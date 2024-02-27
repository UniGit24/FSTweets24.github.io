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
import re

june_no = 0
july_no = 0
jan_no = 0
feb_no = 0
mar_no = 0
apr_no = 0
may_no = 0
june_found = 0
july_found = 0
jan_found= 0
feb_found = 0
mar_found = 0
apr_found = 0
may_found = 0

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

    
def main(country, topic, date, arr, lon, lat):
    new_arr = []
    new_lat = []
    new_lon = []
    new_score = []
    temp_no_scores = 0
    for index, x in enumerate(arr, start=1): 
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
        for y in score:
            if y>80:
                temp_index = index - 1
                print(temp_index)
                print(arr)
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
    tweetsfound = len(new_arr)
    print(tweetsfound)
    classA = pd.DataFrame(
    d
    )
    print(classA)

    fig = px.scatter_geo(classA, lat='lat', lon='lon', title='Map', hover_name='text', size='score')
    
    if (country == 'Australia'): 
        fig.update_layout(
            title = ("Number of tweets:" + str(temp_no_scores) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(tweetsfound)),
            geo_scope='world'
        )
        if (date == 'jun 21'):
                global june_no
                global june_found
                june_no = temp_no_scores
                june_found = tweetsfound
        if (date == 'jul 21'):
                global july_no
                global july_found
                july_no = temp_no_scores
                july_found = tweetsfound
        if (date == 'jan 21'):
                global jan_no
                global jan_found
                jan_no = temp_no_scores
                jan_found = tweetsfound
        if (date == 'feb 21'):
                global feb_no
                global feb_found
                feb_no = temp_no_scores
                feb_found = tweetsfound
        if (date == 'mar 21'):
                global mar_no
                global mar_found
                mar_no = temp_no_scores
                mar_found = tweetsfound
        if (date == 'apr 21'):
                global apr_no
                global apr_found
                apr_no = temp_no_scores
                apr_found = tweetsfound        
        if (date == 'may 21'):
                global may_no
                global may_found
                may_no = temp_no_scores
                may_found = tweetsfound
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
    f = open('bloomberg_quint_news (1).json',)
    data = json.load(f)
    # list
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
    f.close()
    for index, x in enumerate(Australia_topics, start=0): 
        y = str(x + str(Australia_dates[index]))
        parseAustraliaTopics.append(y)
    for index, x in enumerate(Canada_topics, start=0): 
        y = str(x + str(Canada_dates[index]))
        parseCanadaTopics.append(y)
    for index, x in enumerate(US_topics, start=0): 
        y = str(x + str(US_dates[index]))
        parseUSTopics.append(y)
    if (country == 'Australia'): 
        for topic in parseAustraliaTopics:
            jan21 = []
            feb21 = []
            mar21 = []
            apr21 = []
            may21 = []
            jun21 = []
            jul21 = []
            file = '2021_July_twitter_trending_data.csv'
            df = pd.read_csv(file)
            df2 = df[df['searched_hashtag_country'] == country] 
            df3 = df2[["searched_hashtag_country","tweet_text","latitude","longitude","user_created_datetime"]]
            file = '2021_June_twitter_trending_data.csv'
            df = pd.read_csv(file)
            df2 = df[df['searched_hashtag_country'] == country] 
            df4 = df2[["searched_hashtag_country","tweet_text","latitude","longitude","user_created_datetime"]]
            file = '2021_September_twitter_trending_data.csv'
            df = pd.read_csv(file)
            df2 = df[df['searched_hashtag_country'] == country] 
            df5 = df2[["searched_hashtag_country","tweet_text","latitude","longitude","user_created_datetime"]]
            file = '2021_October_twitter_trending_data.csv'
            df = pd.read_csv(file)
            df2 = df[df['searched_hashtag_country'] == country] 
            df6 = df2[["searched_hashtag_country","tweet_text","latitude","longitude","user_created_datetime"]]

            df7 = pd.concat([df3, df4, df5, df6], ignore_index=True)

            jan21 = df7[df7['user_created_datetime'].str.contains('01/2021')]
            feb21 = df7[df7['user_created_datetime'].str.contains('02/2021')]
            mar21 = df7[df7['user_created_datetime'].str.contains('03/2021')]
            apr21 = df7[df7['user_created_datetime'].str.contains('04/2021')]
            may21 = df7[df7['user_created_datetime'].str.contains('05/2021')]
            jun21 = df7[df7['user_created_datetime'].str.contains('06/2021')]
            jul21 = df7[df7['user_created_datetime'].str.contains('07/2021')]

            arr = jan21["tweet_text"]
            lat = jan21["latitude"]
            lon = jan21["longitude"]
            date = "jan 21"
            main(country, topic, date, arr, lon, lat)
            arr = feb21["tweet_text"]
            lat = feb21["latitude"]
            lon = feb21["longitude"]
            date = "feb21"
            main(country, topic, date, arr, lon, lat)
            arr = mar21["tweet_text"]
            lat = mar21["latitude"]
            lon = mar21["longitude"]
            date = "mar21"
            main(country, topic, date, arr, lon, lat)
            arr = apr21["tweet_text"]
            lat = apr21["latitude"]
            lon = apr21["longitude"]
            date = "apr21"
            main(country, topic, date, arr, lon, lat)
            arr = may21["tweet_text"]
            lat = may21["latitude"]
            lon = may21["longitude"]
            date = "may21"
            main(country, topic, date, arr, lon, lat)
            arr = jun21["tweet_text"]
            lat = jun21["latitude"]
            lon = jun21["longitude"]
            date = "jun 21"
            main(country, topic, date, arr, lon, lat)
            arr = jul21["tweet_text"]
            lat = jul21["latitude"]
            lon = jul21["longitude"]
            date = "jul 21"
            main(country, topic, date, arr, lon, lat)

            june_percent = ((june_found/june_no)*100)
            july_percent = ((july_found/july_no)*100)
            jan_percent = ((jan_found/jan_no)*100)
            feb_percent = ((feb_found/feb_no)*100)
            mar_percent = ((mar_found/mar_no)*100)
            apr_percent = ((apr_found/apr_no)*100)
            may_percent = ((may_found/may_no)*100)

            List = [[country, topic, jan_percent, feb_percent, mar_percent, apr_percent, may_percent, june_percent,july_percent]]
            print(List)
            with open('FINALAUS.csv', 'a', newline = '') as f_object:
                writer_object = csv.writer(f_object)
                writer_object.writerows(List)
        f_object.close()        


    if (country == 'Canada'): 
        for topic in parseCanadaTopics:
            #topic = "Victoria to enter sixth lockdown"
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
                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = csv.writer(f_object)
        
                # Pass the list as an argument into the writerow()
                writer_object.writerows(List)
        
                # Close the file object
        f_object.close()  

    if (country == 'United States'): 
        for topic in parseUSTopics:
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
            with open('FINALUS.csv', 'a', newline = '') as f_object:
                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = csv.writer(f_object)
        
                # Pass the list as an argument into the writerow()
                writer_object.writerows(List)
        
                # Close the file object
        f_object.close()        




from tkinter import *
from tkinter import ttk 

app = Tk() 
app.geometry("600x400") 

def clear(): 
	combo.set('') 
        
def get_index(*arg): 
    
    initialiser(str(var.get()))

countries = ('Australia', 'Canada', 'United States')  

var = StringVar() 
combo = ttk.Combobox(app, textvariable=var) 
combo['values'] = countries 
combo['state'] = 'readonly'
combo.pack(padx=5, pady=5) 

button = Button(app, text="Next", command=get_index) 
button.pack() 
app.mainloop() 