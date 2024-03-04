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
    print(tweetsfound)
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
    #fig.write_html("austweet1.html")
    #fdf = pd.DataFrame(data=d)
    #fig = px.scatter_geo(fdf, lat='lat', lon='lon', title='Map', hover_name='text', size='score')
    #fig.show()

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
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    # Iterating through the json
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
    # Closing file
    f.close()
    for index, x in enumerate(Australia_topics, start=0): 
        y = str(x + str(Australia_dates[index]))
        print(y)
        parseAustraliaTopics.append(y)
    #USA_topics = ["June 1 - SARS-CoV-2 Delta variant becomes the dominant strain of COVID-19 in the United States", "June 1 - COVID-19 vaccines – Moderna seeks full approval from the FDA for the Moderna COVID-19 vaccine", "June 5 – Aftermath of the January 6 United States Capitol attack – The Department of Justice says that over 465 people have been arrested since the January 6 attack. It is also seeking information on 250 other suspects.", "July 20 - Tom Barrack, founder of Colony Capital and an advisor of Donald Trump, is indicted for making false statements to the FBI and being an unregistered agent for the United Arab Emirates.", "August 2 - COVID-19 vaccination: Over 70% of adults are reported to have received at least one dose of a COVID-19 vaccine.", "August 10 - New York Governor Andrew Cuomo announces he will resign effective August 24 after an inquiry found he sexually harassed multiple women.", "August 29 - Hurricane Ida makes landfall at 11:55am CDT near Port Fourchon, Louisiana, on the 16th anniversary of Hurricane Katrina."]
    for index, x in enumerate(Canada_topics, start=0): 
        y = str(x + str(Canada_dates[index]))
        print(y)
        parseCanadaTopics.append(y)
    for index, x in enumerate(US_topics, start=0): 
        y = str(x + str(US_dates[index]))
        print(y)
        #parseUSTopics.append(y)
        parseUSTopics = ["U.S. Mortgage Rates Slip to Lowest Level in Almost Three Months06 May 2021, 7:30 PM IST",
"EU Ready to Discuss U.S. Plan to Waive Vaccine Patent Protection06 May 2021, 12:51 PM IST",
"McConnell Says U.S. Afghan Withdrawal Means Return of Taliban06 May 2021, 11:27 PM IST",
"China Must Be Responsible for Falling Rocket, U.S. Lawmaker Says07 May 2021, 12:43 AM IST",
"Norwegian Cruise CEO Rules Out July U.S. Start; Shares Drop06 May 2021, 8:55 PM IST",
"U.S. Housing Regulator Eyes Rules to Curb Short-Term Rental Risk07 May 2021, 12:23 AM IST",
"Bitcoin Traders in U.S. Lack Investor Protections, Gensler Says07 May 2021, 12:47 AM IST",
"Japan and South Korea Air Their Differences as U.S. Seeks Unity06 May 2021, 7:56 AM IST",
"U.S. Eviction Moratorium Reinstated While Judge Considers Case06 May 2021, 8:50 AM IST",
"Job Openings at U.S. Small Businesses Increase to Fresh Record06 May 2021, 11:28 PM IST",
"Risk Binge, U.S. Pressures China, Bankers Not to Blame: Eco Day07 May 2021, 4:37 AM IST",
"U.S. Nuclear Weapons Upgrade to See Delay on Old Silos, Tech06 May 2021, 8:35 PM IST",
"U.S. Jobless Claims Fall More Than Forecast to Pandemic Low06 May 2021, 6:06 PM IST",
"U.S. to Strengthen Security Assistance to Ukraine, Blinken Says06 May 2021, 1:17 PM IST",
"Yellen Faces U.S. Debt-Limit Dance, With Covid Complications06 May 2021, 11:30 AM IST",
"‘Job Paradox’ Baffles Economists as U.S. Employers See Shortage06 May 2021, 2:30 PM IST",
"U.S. Says Swift Return to Nuclear Deal Hinges on Iran’s Moves06 May 2021, 10:42 PM IST",
"China, U.S. to Offer Clashing World Views at UN Event Friday07 May 2021, 4:32 AM IST"]
   #Canada_topics = ["June 21 – The Government of Canada announces the first phase to easing the COVID-19 border measures for travellers, thus lifting quarantine requirements for fully immunised travellers starting on July 5", "June 30 - Dozens of people have died amid an unprecedented heatwave that has smashed temperature records.", "July 20 – British Columbia declares a state of emergency in response to the 2021 British Columbia wildfires.", "August 2 -  SARS-CoV-2 Delta variant becomes the pre-dominant strain of COVID-19 in Canada."]
    if (country == 'Australia'): 
        for topic in parseAustraliaTopics:
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
            with open('FINALAUS.csv', 'a', newline = '') as f_object:
                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = csv.writer(f_object)
        
                # Pass the list as an argument into the writerow()
                writer_object.writerows(List)
        
                # Close the file object
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

months = ('Australia', 'Canada', 'United States')  

var = StringVar() 
combo = ttk.Combobox(app, textvariable=var) 
combo['values'] = months 
combo['state'] = 'readonly'
combo.pack(padx=5, pady=5) 

button = Button(app, text="Next", command=get_index) 
button.pack() 
app.mainloop() 



