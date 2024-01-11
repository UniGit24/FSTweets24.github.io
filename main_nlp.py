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
from sentence_transformers import SentenceTransformer, util


def sentance_similarily(topic, tweet):
     
    sentences = [topic,tweet]

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    #Compute embedding for both lists
    embedding_1= model.encode(sentences[0], convert_to_tensor=True)
    embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

    return util.pytorch_cos_sim(embedding_1, embedding_2)
    ## tensor([[0.6003]])

    
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
        score = sentance_similarily(topic,tweet)
        print(score)
        for y in score:
            if y < 0.05:
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