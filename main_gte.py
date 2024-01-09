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
    for index, x in enumerate(arr, start=1): 
        topic = "President Biden calls for Governer Cuomo to resign"
        tweet = x
        score = detector(topic,tweet)
        print(score)
        for y in score:
            if y > 75:
                arr.pop(index)
                lat.pop(index)
                lon.pop(index)

    d = {'text': arr, 'lat': lat, 'lon':lon}
    fdf = pd.DataFrame(data=d)
    print(len(arr))
    fig = px.scatter_geo(fdf, lat='lat', lon='lon', hover_data = 'text', title='Map')
    fig.show()


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