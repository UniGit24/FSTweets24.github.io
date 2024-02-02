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

    
def main(country, topic, file, date):
    print(country, topic, file, date)
    df = pd.read_csv('August21Data.csv')
   # df = pd.read_csv('Book2.csv')
    #df = pd.read_csv(file)
    df2 = df[df['searched_hashtag_country'] == country]
    df3 = df2[["id","searched_hashtag_country","tweet_text","latitude","longitude"]]
    hashcountry = df3["searched_hashtag_country"]
    arr = df3["tweet_text"]
    lat = df3["latitude"]
    lon = df3["longitude"]
    id = df3["id"]
    #hashcountry.index(country)
    tempi = hashcountry.index("Canada")
    print(tempi)
    new_arr = []
    new_lat = []
    new_lon = []
    new_score = []
    temp_no_scores = 0
   # d = {'text': [], 'lat': [], 'lon':[]}
    for index, x in enumerate(arr, start=1): 
        #topic = "Victoria to enter sixth lockdown"
        #topic = "the spirit of god"
        tweet = x
        try:
            score = detector(topic,tweet)
        except:
            index = index + 1
        temp_no_scores = temp_no_scores +1
        print(score)
        index_list = []
        for y in score:
            if y>70:
            #    print()
            #    d["text"].append(x)
            #    latitude = lat[index]
            #    print(latitude)
            #    d["lat"].append(lat[index])
            #    d["lon"].append(lon[index])
                print(index)
                temp_index = id[index] - 1
                #print(temp_index)
                #print(arr)
                #print(id)
                new_arr.append(arr[temp_index])
                new_lat.append(lat[temp_index])
                new_lon.append(lon[temp_index])
                temp_score = y
                new_score.append(((temp_score.item()-65)*5))
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
            title = ("Number of tweets:" + str(temp_no_scores) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(tweetsfound)),
            geo_scope='usa'
        )
    if (country == 'Australia'): 
        fig.update_layout(
            title = ("Number of tweets:" + str(temp_no_scores) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(tweetsfound)),
            geo_scope='world'
        )
    if (country == 'Canada'):   
        fig.update_layout(
            title = ("Number of tweets:" + str(temp_no_scores) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(tweetsfound)),
            geo_scope='north america'
        )
    fig.show()
    filename = topic +".html"
    fig.write_html(filename)
    #fig.write_html("austweet1.html")
    #fdf = pd.DataFrame(data=d)
    #fig = px.scatter_geo(fdf, lat='lat', lon='lon', title='Map', hover_name='text', size='score')
    #fig.show()

def initialiser (country):
    Australia_topics = ["Victoria to enter sixth lockdown","26 June – Greater Sydney, Wollongong, Blue Mountains and the Central Coast are placed into lockdown as the Delta variant of COVID-19 spreads.", " 11 July – Australia records its first death from the COVID-19 pandemic for 2021,as Sydney records 77 cases of community transmission.", "16 July – Melbourne enters snap lockdown with 18 cases of COVID-19.", "21 August – New South Wales records the highest daily COVID-19 case numbers in Australia thus far, recording 825 new cases of COVID-19.","25 August – New South Wales records 1,029 new cases of COVID-19 in 24 hours becoming the first state in Australia to surpass the 1,000 daily case milestone."]
    USA_topics = ["June 1 - SARS-CoV-2 Delta variant becomes the dominant strain of COVID-19 in the United States", "June 1 - COVID-19 vaccines – Moderna seeks full approval from the FDA for the Moderna COVID-19 vaccine", "June 5 – Aftermath of the January 6 United States Capitol attack – The Department of Justice says that over 465 people have been arrested since the January 6 attack. It is also seeking information on 250 other suspects.", "July 20 - Tom Barrack, founder of Colony Capital and an advisor of Donald Trump, is indicted for making false statements to the FBI and being an unregistered agent for the United Arab Emirates.", "August 2 - COVID-19 vaccination: Over 70% of adults are reported to have received at least one dose of a COVID-19 vaccine.", "August 10 - New York Governor Andrew Cuomo announces he will resign effective August 24 after an inquiry found he sexually harassed multiple women.", "August 29 - Hurricane Ida makes landfall at 11:55am CDT near Port Fourchon, Louisiana, on the 16th anniversary of Hurricane Katrina."]
    Canada_topics = ["June 21 – The Government of Canada announces the first phase to easing the COVID-19 border measures for travellers, thus lifting quarantine requirements for fully immunised travellers starting on July 5", "June 30 - Dozens of people have died amid an unprecedented heatwave that has smashed temperature records.", "July 20 – British Columbia declares a state of emergency in response to the 2021 British Columbia wildfires.", "August 2 -  SARS-CoV-2 Delta variant becomes the pre-dominant strain of COVID-19 in Canada."]
    if (country == 'Australia'): 
        for topic in Australia_topics:
            #topic = "Victoria to enter sixth lockdown"
            file = 'August21Data.csv'
            date = 'August 21'
            main(country, topic, file, date)
            file = '2021_July_twitter_trending_data.csv'
            date = 'July 21'
            main(country, topic, file, date)
            file = '2021_June_twitter_trending_data.csv'
            date = 'June 21'
            main(country, topic, file, date)

    if (country == 'Canada'): 
        for topic in Canada_topics:
            #topic = "Victoria to enter sixth lockdown"
            file = 'August21Data.csv'
            date = 'August 21'
            main(country, topic, file, date)
            file = '2021_July_twitter_trending_data.csv'
            date = 'July 21'
            main(country, topic, file, date)
            file = '2021_June_twitter_trending_data.csv'
            date = 'June 21'
            main(country, topic, file, date)

    if (country == 'United States'): 
        for topic in USA_topics:
            #topic = "Victoria to enter sixth lockdown"
            file = 'August21Data.csv'
            date = 'August 21'
            main(country, topic, file, date)
            file = '2021_July_twitter_trending_data.csv'
            date = 'July 21'
            main(country, topic, file, date)
            file = '2021_June_twitter_trending_data.csv'
            date = 'June 21'
            main(country, topic, file, date)
            file = '2021_September_twitter_trending_data.csv'
            date = 'September 21'
            main(country, topic, file, date)
            file = '2021_October_twitter_trending_data.csv'
            date = 'October 21'
            main(country, topic, file, date)


from tkinter import *
from tkinter import ttk 

app = Tk() 
app.geometry("600x400") 

def clear(): 
	combo.set('') 
        
def get_index(*arg): 
    
    initialiser(str(var.get()))

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