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
import json
from csv import writer

june_no = 0
july_no = 0
august_no = 0
september_no = 0
october_no = 0
june_found = 0
july_found = 0
august_found= 0
september_found = 0
october_found = 0

def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

def detector(topic,tweet):
    input_texts = [topic, tweet]

    tokenizer = AutoTokenizer.from_pretrained("thenlper/gte-large")
    model = AutoModel.from_pretrained("thenlper/gte-large")

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
    #df = pd.read_csv('August21Data.csv')
    #df = pd.read_csv('Book2.csv')
    df = pd.read_csv(file)
    df2 = df[df['searched_hashtag_country'] == country]
    df3 = df2[["searched_hashtag_country","tweet_text","latitude","longitude"]]
    print(df3)
    arr = df3["tweet_text"]
    lat = df3["latitude"]
    lon = df3["longitude"]
    #id = df3["id"]
    print(arr)
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
        print(temp_no_scores)
        if temp_no_scores == 100:
            break
        index_list = []
        for y in score:
            if y>80:
            #    print()
            #    d["text"].append(x)
            #    latitude = lat[index]
            #    print(latitude)
            #    d["lat"].append(lat[index])
            #    d["lon"].append(lon[index])
                temp_index = index - 1
                print(temp_index)
                print(arr)
                #print(id)
                #print(arr[temp_index])
                if (country == "United States" ):
                    if (date == 'August 21'):
                        temp_index = temp_index + 23130
                    if (date == 'July 21'):
                        temp_index = temp_index + 7634
                    if (date == 'June 21'):
                        temp_index = temp_index + 34212
                    if (date == 'September 21'):
                        temp_index = temp_index + 7618
                    if (date == 'October 21'):
                        temp_index = temp_index + 5960
                try:
                    new_arr.append(arr[temp_index])
                    new_lat.append(lat[temp_index])
                    new_lon.append(lon[temp_index])
                    temp_score = y
                    new_score.append(((temp_score.item()-75)*5))
                    print(new_arr)
                except:
                    index = index + 1

    d = {"text": new_arr, "lat": new_lat, "lon": new_lon, "score": new_score}
    d_columns = ['text', 'lat', 'lon', 'score']
    tweetsfound = len(new_arr)
    print(tweetsfound)
    classA = pd.DataFrame(
    d
    )
    print(classA)
    fig = px.scatter_geo(classA, lat='lat', lon='lon', title='Map', hover_name='text', size='score')
    #country selecter
    
    if (country == 'Australia'): 
        fig.update_layout(
            title = ("Number of tweets:" + str(temp_no_scores) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(tweetsfound)),
            geo_scope='world'
        )
        if (date == 'June 21'):
                global june_no
                global june_found
                june_no = temp_no_scores
                june_found = tweetsfound
        if (date == 'July 21'):
                global july_no
                global july_found
                july_no = temp_no_scores
                july_found = tweetsfound
        if (date == 'August 21'):
                global august_no
                global august_found
                august_no = temp_no_scores
                august_found = tweetsfound
        if (date == 'September 21'):
                global september_no
                global september_found
                september_no = temp_no_scores
                september_found = tweetsfound
        if (date == 'October 21'):
                global october_no
                global october_found
                october_no = temp_no_scores
                october_found = tweetsfound
    if (country == 'Canada'):   
        fig.update_layout(
            title = ("Number of tweets:" + str(temp_no_scores) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(tweetsfound)),
            geo_scope='north america'
        )
        if (date == 'June 21'):
                june_no
                june_found
                june_no = temp_no_scores
                june_found = tweetsfound
        if (date == 'July 21'):
                july_no
                july_found
                july_no = temp_no_scores
                july_found = tweetsfound
        if (date == 'August 21'):
                august_no
                august_found
                august_no = temp_no_scores
                august_found = tweetsfound
        if (date == 'September 21'):
                september_no
                september_found
                september_no = temp_no_scores
                september_found = tweetsfound
        if (date == 'October 21'):
                october_no
                october_found
                october_no = temp_no_scores
                october_found = tweetsfound
    if (country == 'United States'):   
        fig.update_layout(
            title = ("Number of tweets:" + str(temp_no_scores) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(tweetsfound)),
            geo_scope='usa'
        )
        if (date == 'June 21'):
                june_no
                june_found
                june_no = temp_no_scores
                june_found = tweetsfound
        if (date == 'July 21'):
                july_no
                july_found
                july_no = temp_no_scores
                july_found = tweetsfound
        if (date == 'August 21'):
                august_no
                august_found
                august_no = temp_no_scores
                august_found = tweetsfound
        if (date == 'September 21'):
                september_no
                september_found
                september_no = temp_no_scores
                september_found = tweetsfound
        if (date == 'October 21'):
                october_no
                october_found
                october_no = temp_no_scores
                october_found = tweetsfound
    fig.show()
    filename = topic + date +".html"
    fig.write_html(filename)

def initialiser (country):
    Australia_topics = []
    Australia_dates = []
    parseAustraliaTopics = []
    Canada_topics = []
    Canada_dates = []
    parseCanadaTopics = []
    US_topics = []
    US_dates = []
    parseUSTopics = []
    # Opening JSON file
    f = open('bloomberg_quint_news (1).json',)
    data = json.load(f)
    for i in data['news']:
        if "Australia" in i['title']:
            if "June 2021" or "July 2021" or "August 2021" or "Septemebr 2021" or "October 2021" in i['date_created']:
                Australia_topics.append(i['title'])
                Australia_dates.append(i['date_created'])
                print(i['title'])
            else:
                print(" ")
        if "U.S." in i['title']:
            if "June 2021" or "July 2021" or "August 2021" or "Septemebr 2021" or "October 2021" in i['date_created']:
                US_topics.append(i['title'])
                US_dates.append(i['date_created'])
                print(i['title'])
            else:
                print(" ")
        if "Canada" in i['title']:
            if "June 2021" or "July 2021" or "August 2021" or "Septemebr 2021" or "October 2021" in i['date_created']:
                Canada_topics.append(i['title'])
                Canada_dates.append(i['date_created'])
                print(i['title'])
            else:
                print(" ")
    # Closing file
    f.close()
    for index, x in enumerate(Australia_topics, start=0): 
        y = str(x + str(Australia_dates[index]))
        print(y)
        parseAustraliaTopics.append(y)
    for index, x in enumerate(Canada_topics, start=0): 
        y = str(x + str(Canada_dates[index]))
        print(y)
        parseCanadaTopics.append(y)
    for index, x in enumerate(US_topics, start=0): 
        y = str(x + str(US_dates[index]))
        print(y)
        parseUSTopics.append(y)
    if (country == 'Australia'): 
        for topic in parseAustraliaTopics:
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

            # List that we want to add as a new row
            june_percent = ((june_found/june_no)*100)
            july_percent = ((july_found/july_no)*100)
            august_percent = ((august_found/august_no)*100)
            september_percent = ((september_found/september_no)*100)
            october_percent = ((october_found/october_no)*100)

            List = [[country,topic,june_no,june_found,june_percent,july_no,july_found,july_percent,august_no,august_found,august_percent,september_no,september_found,september_percent,october_no,october_found,october_percent]]
            print(List)
            # Open our existing CSV file in append mode
            # Create a file object for this file
            with open('FINALAUS.csv', 'a', newline = '') as f_object:

                writer_object = csv.writer(f_object)
        
                writer_object.writerows(List)
        
        f_object.close()        


    if (country == 'Canada'): 
        for topic in parseCanadaTopics:
            file = 'August21Datacan.csv'
            date = 'August 21'
            main(country, topic, file, date)
            file = '2021_July_twitter_trending_datacan.csv'
            date = 'July 21'
            main(country, topic, file, date)
            file = '2021_June_twitter_trending_datacan.csv'
            date = 'June 21'
            main(country, topic, file, date)
            file = '2021_September_twitter_trending_datacan.csv'
            date = 'September 21'
            main(country, topic, file, date)
            file = '2021_October_twitter_trending_datacan.csv'
            date = 'October 21'
            main(country, topic, file, date)

            # List that we want to add as a new row
            june_percent = ((june_found/june_no)*100)
            july_percent = ((july_found/july_no)*100)
            august_percent = ((august_found/august_no)*100)
            september_percent = ((september_found/september_no)*100)
            october_percent = ((october_found/october_no)*100)

            List = [[country,topic,june_no,june_found,june_percent,july_no,july_found,july_percent,august_no,august_found,august_percent,september_no,september_found,september_percent,october_no,october_found,october_percent]]
            print(List)
            # Open our existing CSV file in append mode
            # Create a file object for this file
            with open('FINALCAN.csv', 'a', newline = '') as f_object:

                writer_object = csv.writer(f_object)
        
                writer_object.writerows(List)
        
        f_object.close()  

    if (country == 'United States'): 
        for topic in parseUSTopics:
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

            june_percent = ((june_found/june_no)*100)
            july_percent = ((july_found/july_no)*100)
            august_percent = ((august_found/august_no)*100)
            september_percent = ((september_found/september_no)*100)
            october_percent = ((october_found/october_no)*100)

            List = [[country,topic,june_no,june_found,june_percent,july_no,july_found,july_percent,august_no,august_found,august_percent,september_no,september_found,september_percent,october_no,october_found,october_percent]]
            print(List)
            # Open our existing CSV file in append mode
            # Create a file object for this file
            with open('FINALUS.csv', 'a', newline = '') as f_object:

                writer_object = csv.writer(f_object)
        
                writer_object.writerows(List)
        
        f_object.close()        




from tkinter import *
from tkinter import ttk 

app = Tk() 
app.geometry("600x400") 

def clear(): 
	combo.set('') 
        
def get_index(*arg): 
    
    initialiser(str(var.get()))

months = ('Australia', 'Canada', 'United States')  

var = StringVar() 
combo = ttk.Combobox(app, textvariable=var) 
combo['values'] = months 
combo['state'] = 'readonly'
combo.pack(padx=5, pady=5) 

button = Button(app, text="Next", command=get_index) 
button.pack() 
app.mainloop() 