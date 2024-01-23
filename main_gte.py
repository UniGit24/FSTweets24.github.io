import plotly.express as px
import pandas as pd
from tkinter import *
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModel
import numpy as np
import csv
import tkinter as tk 
from tkinter import ttk 
import plotly.graph_objects as go



def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

def detector(topic,tweet):
    input_texts = [topic, tweet]

    tokenizer = AutoTokenizer.from_pretrained("thenlper/gte-small")
    model = AutoModel.from_pretrained("thenlper/gte-small")

    # Tokenize the input texts
    batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

    outputs = model(**batch_dict)
    embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

    # (Optionally) normalize embeddings
    embeddings = F.normalize(embeddings, p=2, dim=1)
    scores = (embeddings[:1] @ embeddings[1:].T) * 100
    return (scores)

    
def main(country):
    #df = pd.read_csv('August21Data.csv')
    df = pd.read_csv('Book2.csv')
    df2 = df[df['searched_hashtag_country'] == country]
    df3 = df2[["id","searched_hashtag_country","tweet_text","latitude","longitude"]]
    arr = df3["tweet_text"]
    lat = df3["latitude"]
    lon = df3["longitude"]
    print(arr)
    new_arr = []
    new_lat = []
    new_lon = []
    new_score = []
   # d = {'text': [], 'lat': [], 'lon':[]}
    for index, x in enumerate(arr, start=1): 
        topic = "Victoria to enter sixth lockdown"
        #topic = "the spirit of god"
        tweet = x
        score = detector(topic,tweet)
        print(score)
        index_list = []
        for y in score:
            if y>75:
            #    print()
            #    d["text"].append(x)
            #    latitude = lat[index]
            #    print(latitude)
            #    d["lat"].append(lat[index])
            #    d["lon"].append(lon[index])
                temp_index = index - 1
                new_arr.append(arr[temp_index])
                new_lat.append(lat[temp_index])
                new_lon.append(lon[temp_index])
                temp_score = y
                new_score.append(temp_score.item())
    #for index, x in enumerate(arr, start=1): 
        #for y in index_list:
            #if y == index:
                #print(index)
               # print(y)
               # temp_index = index - 1
              #  print(temp_index)
              #  print(arr[temp_index])
              #  new_arr.append(arr[temp_index])
              #  new_lat.append(lat[temp_index])
              #  new_lon.append(lon[temp_index])
    #for x in index_list:
    #    temp_index = x - 1
    #    new_arr.append(arr[temp_index])
    #    new_lat.append(lat[temp_index])
    #    new_lon.append(lon[temp_index])
    d = {"text": new_arr, "lat": new_lat, "lon": new_lon, "score": new_score}
    d_columns = ['text', 'lat', 'lon', 'score']
    tweetsfound = len(new_arr)
    classA = pd.DataFrame(
    d
    )
    print(classA)
#save dataframe to csv file
   # classA.to_csv("student.csv", index=False)
    #print(d)
    #with open("test.csv", "w") as outfile:
       # linker = csv.DictWriter(outfile, fieldnames = d_columns)
        #linker.writeheader()
        #for x in d_columns:
        #    linker.writerow(x)
        #writer = csv.DictWriter(outfile, fieldnames=d_columns)
       # writer.writeheader()
       # for data in d:
        #    writer.writerow(data)
        #w = csv.DictWriter(outfile, d.keys())
        #w.writeheader()
        #w.writerow(d)
        #writer = csv.writer(outfile)
        #key_list = list(d.keys())
        #limit = len(d)
        #writer.writerow(d.keys())
        #for i in range(limit):
            #writer.writerow([d[x][i] for x in key_list])
    #dt = pd.read_csv('test.csv')
    #print(dt)
    #fig = go.Figure(data=go.Scattergeo(lon = dt['lon'],lat = dt['lat'],text = dt['text'], mode = 'markers',size = dt['score']))
    #fig = px.scatter_geo(dt, lat='lat', lon='lon', title='Map', hover_name='text', size='score')

    fig = px.scatter_geo(classA, lat='lat', lon='lon', title='Map', hover_name='text', size='score')
    #country selecter
    if (country == 'United States'): 
        fig.update_layout(
            title = ("Tweets found: {}".format(tweetsfound)),
            geo_scope='usa',
        )
    if (country == 'Australia'): 
        fig.update_layout(
            title = ("Tweets found: {}".format(tweetsfound)),
            geo_scope='world',
        )
    if (country == 'Canada'):   
        fig.update_layout(
            title = ("Tweets found: {}".format(tweetsfound)),
            geo_scope='north america',
        )
    fig.show()
    fig.write_html("austweet1.html")
    #fdf = pd.DataFrame(data=d)
    #fig = px.scatter_geo(fdf, lat='lat', lon='lon', title='Map', hover_name='text', size='score')
    #fig.show()


from tkinter import *
from tkinter import ttk 

app = Tk() 
app.geometry("600x400") 

def clear(): 
	combo.set('') 
        
def get_index(*arg): 
    main(str(var.get()))

months = ('Australia', 
						'Brazil', 
						'Canada', 
						'France', 
						'Germany', 
						'India', 
						'Italy', 
						'Mexico', 
						'Ukraine', 
						'United States')  

var = StringVar() 
combo = ttk.Combobox(app, textvariable=var) 
combo['values'] = months 
combo['state'] = 'readonly'
combo.pack(padx=5, pady=5) 

button = Button(app, text="Next", command=get_index) 
button.pack() 
app.mainloop() 