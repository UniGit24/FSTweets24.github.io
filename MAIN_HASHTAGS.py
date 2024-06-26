import plotly.express as px
import pandas as pd
from tkinter import *
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModel
import numpy as np
import csv
from tkinter import *
from tkinter import ttk 
import plotly.graph_objects as go
import json
from csv import writer
import re
from collections import Counter


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
june_hash = 0
july_hash = 0
jan_hash = 0
feb_hash = 0
mar_hash = 0
apr_hash = 0
may_hash = 0
june_dates = []
july_dates = []
jan_dates = []
feb_dates = []
mar_dates = []
apr_dates = []
may_dates = []


def find_most_common_hashtags(texts):
    hashtags = []
    for text in texts:
        found_hashtags = re.findall(r'#(\w+)', text)
        hashtags.extend(found_hashtags)
    hashtag_counter = Counter(hashtags)
    most_common_hashtags = hashtag_counter.most_common()
    return most_common_hashtags

def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

def detector(topic,tweet):
    input_texts = [topic, tweet]

    tokenizer = AutoTokenizer.from_pretrained("thenlper/gte-large")
    model = AutoModel.from_pretrained("thenlper/gte-large")

    batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

    outputs = model(**batch_dict)
    embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

    embeddings = F.normalize(embeddings, p=2, dim=1)
    scores = (embeddings[:1] @ embeddings[1:].T) * 100
    return (scores)

    
def main(country, topic, date, arr, lon, lat,created_date):
    new_arr = []
    new_lat = []
    new_lon = []
    new_score = []
    temp_no_scores = 0
    maintweets = 0
    new_date = []
    for index, x in enumerate(arr, start=1): 
        tweet = x
        try:
            score = detector(topic,tweet)
        except:
            index = index + 1
        temp_no_scores = temp_no_scores +1
        print(score)
        print(temp_no_scores)
        for y in score:
            if y>80:
                maintweets = maintweets + 1
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
                items_list = list(arr.items())
                print(items_list[temp_index])
                try:
                    items_list = list(arr.items())
                    new_arr.append(items_list[temp_index])
                    items_list = list(lat.items())
                    new_lat.append(items_list[temp_index])
                    items_list = list(lon.items())
                    new_lon.append(items_list[temp_index])
                    items_list = list(created_date.items())
                    new_date.append(items_list[temp_index])
                    temp_score = y
                    new_score.append(((temp_score.item()-75)*5))
                    print(new_arr, new_lat, new_lon, new_date)
                    print([item[1] for item in new_arr])
                    print(new_score)
                except:
                    index = index + 1


    texts_list = [str(item) for item in new_arr]
    most_common_hashtags = find_most_common_hashtags(texts_list)
    hashtagcount = 0
    for hashtag, count in most_common_hashtags:
        if count >= 2:
            for index, element in enumerate(arr):
                if hashtag in element:
                    items_list = list(arr.items())
                    new_arr.append(items_list[index])
                    items_list = list(lat.items())
                    new_lat.append(items_list[index])
                    items_list = list(created_date.items())
                    new_date.append(items_list[index])
                    items_list = list(lon.items())
                    new_lon.append(items_list[index])
                    new_score.append(((80-75)*5))
                    hashtagcount = hashtagcount + 1

    date_numbers = []
    for item in new_date:
        match = re.match(r'(\d{2})/', item[1])  
        if match:
            date_numbers.append(int(match.group(1)))  
    print(date_numbers)

    d = {"text": [item[1] for item in new_arr], "lat": [item[1] for item in new_lat], "lon": [item[1] for item in new_lon],"score": new_score}
    totalcount = 0
    for x in new_arr:
        totalcount = totalcount + 1
    print(len(new_arr), maintweets, totalcount)
    tweetsfound = len(new_arr) - maintweets

    print(tweetsfound)
    print(new_arr)
    classA = pd.DataFrame(
    d
    )
    print(classA)

    fig = px.scatter_geo(classA, lat='lat', lon='lon', title='Map', hover_name='text', size='score')
    print()
    if (country == 'Australia'): 
        fig.update_layout(
            title = ("Number of tweets:" + str(len(arr)) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(totalcount)),
            geo_scope='world'
        )
        if (date == 'jun 21'):
                global june_no
                global june_found
                global june_hash
                global june_dates
                june_dates = date_numbers
                june_hash = hashtagcount
                june_no = len(arr)
                june_found = totalcount
        if (date == 'jul 21'):
                global july_no
                global july_found
                global july_hash
                global july_dates
                july_dates = date_numbers
                july_hash = hashtagcount
                july_no = len(arr)
                july_found = totalcount
        if (date == 'jan 21'):
                global jan_no
                global jan_found
                global jan_hash
                global jan_dates
                jan_dates = date_numbers
                jan_hash = hashtagcount
                jan_no = len(arr)
                jan_found = totalcount
                print(jan_found,jan_no)
        if (date == 'feb21'):
                global feb_no
                global feb_found
                global feb_hash
                global feb_dates
                feb_dates = date_numbers
                feb_hash = hashtagcount
                feb_no = len(arr)
                feb_found = totalcount
                print(feb_found,feb_no)
        if (date == 'mar21'):
                global mar_no
                global mar_found
                global mar_hash
                global mar_dates
                mar_dates = date_numbers
                mar_hash = hashtagcount
                mar_no = len(arr)
                mar_found = totalcount
        if (date == 'apr21'):
                global apr_no
                global apr_found
                global apr_hash
                global apr_dates
                apr_dates = date_numbers
                apr_hash = hashtagcount
                apr_no = len(arr)
                apr_found = totalcount        
        if (date == 'may21'):
                global may_no
                global may_found
                global may_hash
                global may_dates
                may_dates = date_numbers
                may_hash = hashtagcount
                may_no = len(arr)
                may_found = totalcount
    if (country == 'Canada'):   
        fig.update_layout(
            title = ("Number of tweets:" + str(len(arr)) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(totalcount)),
            geo_scope='north america'
        )
        if (date == 'jun 21'):
                june_no
                june_found
                june_hash
                june_dates
                june_dates = date_numbers
                june_hash = hashtagcount
                june_no = len(arr)
                june_found = totalcount
        if (date == 'jul 21'):
                july_no
                july_found
                july_hash
                july_dates
                july_dates = date_numbers
                july_hash = hashtagcount
                july_no = len(arr)
                july_found = totalcount
        if (date == 'jan 21'):
                jan_no
                jan_found
                jan_hash
                jan_dates
                jan_dates = date_numbers
                jan_hash = hashtagcount
                jan_no = len(arr)
                jan_found = totalcount
                print(jan_found,jan_no)
        if (date == 'feb21'):
                feb_no
                feb_found
                feb_hash
                feb_dates
                feb_dates = date_numbers
                feb_hash = hashtagcount
                feb_no = len(arr)
                feb_found = totalcount
                print(feb_found,feb_no)
        if (date == 'mar21'):
                mar_no
                mar_found
                mar_hash
                mar_dates
                mar_dates = date_numbers
                mar_hash = hashtagcount
                mar_no = len(arr)
                mar_found = totalcount
        if (date == 'apr21'):
                apr_no
                apr_found
                apr_hash
                apr_dates
                apr_dates = date_numbers
                apr_hash = hashtagcount
                apr_no = len(arr)
                apr_found = totalcount        
        if (date == 'may21'):
                may_no
                may_found
                may_hash
                may_dates
                may_dates = date_numbers
                may_hash = hashtagcount
                may_no = len(arr)
                may_found = totalcount
    if (country == 'United States'):   
        fig.update_layout(
            title = ("Number of tweets:" + str(len(arr)) + " Date: " + str(date) + " " + topic + "Tweets found: {}".format(totalcount)),
            geo_scope='usa'
        )
        if (date == 'jun 21'):
                june_no
                june_found
                june_hash
                june_dates
                june_dates = date_numbers
                june_hash = hashtagcount
                june_no = len(arr)
                june_found = totalcount
        if (date == 'jul 21'):
                july_no
                july_found
                july_hash
                july_dates
                july_dates = date_numbers
                july_hash = hashtagcount
                july_no = len(arr)
                july_found = totalcount
        if (date == 'jan 21'):
                jan_no
                jan_found
                jan_hash
                jan_dates
                jan_dates = date_numbers
                jan_hash = hashtagcount
                jan_no = len(arr)
                jan_found = totalcount
                print(jan_found,jan_no)
        if (date == 'feb21'):
                feb_no
                feb_found
                feb_hash
                feb_dates
                feb_dates = date_numbers
                feb_hash = hashtagcount
                feb_no = len(arr)
                feb_found = totalcount
                print(feb_found,feb_no)
        if (date == 'mar21'):
                mar_no
                mar_found
                mar_hash
                mar_dates
                mar_dates = date_numbers
                mar_hash = hashtagcount
                mar_no = len(arr)
                mar_found = totalcount
        if (date == 'apr21'):
                apr_no
                apr_found
                apr_hash
                apr_dates
                apr_dates = date_numbers
                apr_hash = hashtagcount
                apr_no = len(arr)
                apr_found = totalcount        
        if (date == 'may21'):
                may_no
                may_found
                may_hash
                may_dates
                may_dates = date_numbers
                may_hash = hashtagcount
                may_no = len(arr)
                may_found = totalcount
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
        print(y)
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
            created_date = jan21["user_created_datetime"]
            date = "jan 21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = feb21["tweet_text"]
            lat = feb21["latitude"]
            lon = feb21["longitude"]
            created_date = feb21["user_created_datetime"]
            date = "feb21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = mar21["tweet_text"]
            lat = mar21["latitude"]
            lon = mar21["longitude"]
            created_date = mar21["user_created_datetime"]
            date = "mar21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = apr21["tweet_text"]
            lat = apr21["latitude"]
            lon = apr21["longitude"]
            created_date = apr21["user_created_datetime"]
            date = "apr21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = may21["tweet_text"]
            lat = may21["latitude"]
            lon = may21["longitude"]
            created_date = may21["user_created_datetime"]
            date = "may21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = jun21["tweet_text"]
            lat = jun21["latitude"]
            lon = jun21["longitude"]
            created_date = jun21["user_created_datetime"]
            date = "jun 21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = jul21["tweet_text"]
            lat = jul21["latitude"]
            lon = jul21["longitude"]
            created_date = jul21["user_created_datetime"]
            date = "jul 21"
            main(country, topic, date, arr, lon, lat,created_date)

            if (june_found != 0):
                june_percent = ((june_found/june_no)*100)
                print(june_percent)
            else:
                june_percent = 0

            if (july_found != 0):
                july_percent = ((july_found/july_no)*100)
            else:
                july_percent = 0

            if (jan_found != 0):
                jan_percent = ((jan_found/jan_no)*100)
            else:
                jan_percent = 0

            if (feb_found != 0):
                feb_percent = ((feb_found/feb_no)*100)
                print(feb_percent)
            else:
                feb_percent = 0

            if (mar_found != 0):
                mar_percent = ((mar_found/mar_no)*100)
            else:
                mar_percent = 0

            if (apr_found != 0):
                apr_percent = ((apr_found/apr_no)*100)
            else:
                apr_percent = 0

            if (may_found != 0):
                may_percent = ((may_found/may_no)*100)
            else:
                may_percent = 0

            print(S)
            List = [country, topic, jan_found, jan_no, jan_percent,feb_found, feb_no, feb_percent,mar_found, mar_no, mar_percent, apr_found, apr_no, apr_percent,may_found, may_no,  may_percent, june_found, june_no, june_percent,july_found, july_no, july_percent, jan_hash, feb_hash, mar_hash, apr_hash, june_hash, july_hash,  jan_dates,feb_dates, mar_dates,apr_dates,may_dates,june_dates,july_dates]
            print(List)
            with open('FINALAUS2.csv', 'a', newline = '') as f_object:
                writer_object = csv.writer(f_object)
                writer_object.writerow(List)
            f_object.close()  


    if (country == 'Canada'): 
        for topic in parseCanadaTopics:
            jan21 = []
            feb21 = []
            mar21 = []
            apr21 = []
            may21 = []
            jun21 = []
            jul21 = []
            file = '2021_July_twitter_trending_datacan.csv' 
            df = pd.read_csv(file)
            df2 = df[df['searched_hashtag_country'] == country] 
            df3 = df2[["searched_hashtag_country","tweet_text","latitude","longitude","user_created_datetime"]]
            file = '2021_June_twitter_trending_datacan.csv'
            df = pd.read_csv(file)
            df2 = df[df['searched_hashtag_country'] == country] 
            df4 = df2[["searched_hashtag_country","tweet_text","latitude","longitude","user_created_datetime"]]
            file = '2021_September_twitter_trending_datacan.csv'
            df = pd.read_csv(file)
            df2 = df[df['searched_hashtag_country'] == country] 
            df5 = df2[["searched_hashtag_country","tweet_text","latitude","longitude","user_created_datetime"]]
            file = '2021_October_twitter_trending_datacan.csv'
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
            created_date = jan21["user_created_datetime"]
            date = "jan 21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = feb21["tweet_text"]
            lat = feb21["latitude"]
            lon = feb21["longitude"]
            created_date = feb21["user_created_datetime"]
            date = "feb21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = mar21["tweet_text"]
            lat = mar21["latitude"]
            lon = mar21["longitude"]
            created_date = mar21["user_created_datetime"]
            date = "mar21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = apr21["tweet_text"]
            lat = apr21["latitude"]
            lon = apr21["longitude"]
            created_date = apr21["user_created_datetime"]
            date = "apr21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = may21["tweet_text"]
            lat = may21["latitude"]
            lon = may21["longitude"]
            created_date = may21["user_created_datetime"]
            date = "may21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = jun21["tweet_text"]
            lat = jun21["latitude"]
            lon = jun21["longitude"]
            created_date = jun21["user_created_datetime"]
            date = "jun 21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = jul21["tweet_text"]
            lat = jul21["latitude"]
            lon = jul21["longitude"]
            created_date = jul21["user_created_datetime"]
            date = "jul 21"
            main(country, topic, date, arr, lon, lat,created_date)

            if (june_found != 0):
                june_percent = ((june_found/june_no)*100)
                print(june_percent)
            else:
                june_percent = 0

            if (july_found != 0):
                july_percent = ((july_found/july_no)*100)
            else:
                july_percent = 0

            if (jan_found != 0):
                jan_percent = ((jan_found/jan_no)*100)
            else:
                jan_percent = 0

            if (feb_found != 0):
                feb_percent = ((feb_found/feb_no)*100)
                print(feb_percent)
            else:
                feb_percent = 0

            if (mar_found != 0):
                mar_percent = ((mar_found/mar_no)*100)
            else:
                mar_percent = 0

            if (apr_found != 0):
                apr_percent = ((apr_found/apr_no)*100)
            else:
                apr_percent = 0

            if (may_found != 0):
                may_percent = ((may_found/may_no)*100)
            else:
                may_percent = 0

            print(country, topic, jan_found, jan_no, jan_percent,feb_found, feb_no, feb_percent,mar_found, mar_no, mar_percent, apr_found, apr_no, apr_percent,may_found, may_no,  may_percent, june_found, june_no, june_percent,july_found, july_no, july_percent, jan_hash, feb_hash, mar_hash, apr_hash, june_hash, july_hash, jan_dates,feb_dates, mar_dates,apr_dates,may_dates,june_dates,july_dates)
            List = [country, topic, jan_found, jan_no, jan_percent,feb_found, feb_no, feb_percent,mar_found, mar_no, mar_percent, apr_found, apr_no, apr_percent,may_found, may_no,  may_percent, june_found, june_no, june_percent,july_found, july_no, july_percent, jan_hash, feb_hash, mar_hash, apr_hash, june_hash, july_hash,  jan_dates,feb_dates, mar_dates,apr_dates,may_dates,june_dates,july_dates]
            print(List)
            with open('FINALCAN1.csv', 'a', newline = '') as f_object:
                writer_object = csv.writer(f_object)
                writer_object.writerow(List)
            f_object.close() 

    if (country == 'United States'): 
        for topic in parseUSTopics:
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
            created_date = jan21["user_created_datetime"]
            date = "jan 21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = feb21["tweet_text"]
            lat = feb21["latitude"]
            lon = feb21["longitude"]
            created_date = feb21["user_created_datetime"]
            date = "feb21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = mar21["tweet_text"]
            lat = mar21["latitude"]
            lon = mar21["longitude"]
            created_date = mar21["user_created_datetime"]
            date = "mar21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = apr21["tweet_text"]
            lat = apr21["latitude"]
            lon = apr21["longitude"]
            created_date = apr21["user_created_datetime"]
            date = "apr21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = may21["tweet_text"]
            lat = may21["latitude"]
            lon = may21["longitude"]
            created_date = may21["user_created_datetime"]
            date = "may21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = jun21["tweet_text"]
            lat = jun21["latitude"]
            lon = jun21["longitude"]
            created_date = jun21["user_created_datetime"]
            date = "jun 21"
            main(country, topic, date, arr, lon, lat,created_date)
            arr = jul21["tweet_text"]
            lat = jul21["latitude"]
            lon = jul21["longitude"]
            created_date = jul21["user_created_datetime"]
            date = "jul 21"
            main(country, topic, date, arr, lon, lat,created_date)

            if (june_found != 0):
                june_percent = ((june_found/june_no)*100)
                print(june_percent)
            else:
                june_percent = 0

            if (july_found != 0):
                july_percent = ((july_found/july_no)*100)
            else:
                july_percent = 0

            if (jan_found != 0):
                jan_percent = ((jan_found/jan_no)*100)
            else:
                jan_percent = 0

            if (feb_found != 0):
                feb_percent = ((feb_found/feb_no)*100)
                print(feb_percent)
            else:
                feb_percent = 0

            if (mar_found != 0):
                mar_percent = ((mar_found/mar_no)*100)
            else:
                mar_percent = 0

            if (apr_found != 0):
                apr_percent = ((apr_found/apr_no)*100)
            else:
                apr_percent = 0

            if (may_found != 0):
                may_percent = ((may_found/may_no)*100)
            else:
                may_percent = 0

            print(country, topic, jan_found, jan_no, jan_percent,feb_found, feb_no, feb_percent,mar_found, mar_no, mar_percent, apr_found, apr_no, apr_percent,may_found, may_no,  may_percent, june_found, june_no, june_percent,july_found, july_no, july_percent, jan_hash, feb_hash, mar_hash, apr_hash, june_hash, july_hash, jan_dates,feb_dates, mar_dates,apr_dates,may_dates,june_dates,july_dates)
            List = [country, topic, jan_found, jan_no, jan_percent,feb_found, feb_no, feb_percent,mar_found, mar_no, mar_percent, apr_found, apr_no, apr_percent,may_found, may_no,  may_percent, june_found, june_no, june_percent,july_found, july_no, july_percent, jan_hash, feb_hash, mar_hash, apr_hash, june_hash, july_hash,  jan_dates,feb_dates, mar_dates,apr_dates,may_dates,june_dates,july_dates]
            print(List)

            with open('FINALUS1.csv', 'a', newline = '') as f_object:
                writer_object = csv.writer(f_object)
                writer_object.writerow(List)
            f_object.close() 





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