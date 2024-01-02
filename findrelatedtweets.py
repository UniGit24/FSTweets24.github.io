import plotly.express as px
import pandas as pd
from tkinter import *
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModel
import numpy as np
import csv


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
    #print(scores.tolist())

def main(fig):
    #df = pd.read_csv('August21Data.csv')
    df = pd.read_csv('Book2.csv')
    df2 = df[df['searched_hashtag_country'] == 'United States']
    df3 = df2[["id","searched_hashtag_country","tweet_text","latitude","longitude"]]
    arr = df3["tweet_text"]
    lat = df3["latitude"]
    lon = df3["longitude"]
    #print(arr)
    for index, x in enumerate(arr, start=1):   
        #print(index, x)
        #for x in arr:
        topic = "new york"
        tweet = x
        #detector(topic,tweet)
        score = detector(topic,tweet)
        for y in score:
            if y < 75:
                arr.pop(index)
                lat.pop(index)
                lon.pop(index)
                #df3= df3.remove_row([index])
                #df3 = df3.remove(next(i for i in df3 if x in i))
                #df3.pop(index)
                #df3.pop(x)

    d = {'text': arr, 'lat': lat, 'lon':lon}
    fdf = pd.DataFrame(data=d)
    print(fdf)

    #fields = ["tweet_text","latitude","longitude"]  
    #columns = [arr,lat,lon]  
    #filename = "newcsv2.csv"
    #count = len(arr)
    #for x in range (0,count):
      #      csvwriter = csv.writer(csvfile) 
       #     csvwriter.writerow(fields) 
       #     new_array = []
       #     print(arr[x])
       #     new_tweet = arr[x]
       #     new_lat = lat[x]
        #    new_lon = lon[x]
        #    new_array.append(new_tweet)
        #    new_array.append(new_lat)
        #    new_array.append(new_lon)
        #    csvwriter.writerow(new_array) 


   # arr1 = np.array([arr], dtype=object)
   # arr2 = np.array([lat], dtype=object)
   # arr3 = np.array([lon], dtype=object)
   # count = len(arr1)
   # result = []
   # for x in range (0,count):
    #    result.append([arr1,arr2,arr3])
    #fin_array = np.stack((arr1, arr2, arr3), axis=1)
   # print(result)
   # data = pd.read_csv(filename)

    fig = px.scatter_geo(fdf, lat='lat', lon='lon', hover_data = 'text', title='Map')

    #fig = px.scatter_geo(df3, lat='latitude', lon='longitude', hover_name = 'searched_hashtag_country', hover_data = 'tweet_text', title='Map')
    fig.show()


def showmap():
    window = Toplevel(root)
    window.title("Map")
    
    fig = px.scatter_geo()
    main(fig)

# create a tkinter window
root = Tk()              
# Open window having dimension 1000x1000
root.geometry('1000x1000') 
# Create a Button
btn = Button(root, text = 'Show map', bd = '5', command = showmap) 
# Set the position of button on the top of window.   
btn.pack(side = 'top')    
root.mainloop()

