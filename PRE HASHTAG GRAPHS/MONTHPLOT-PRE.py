from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd
from pandas import *



df = pd.read_csv('FINALAUS1.csv')

topic_list = df["topic"]
countries = df["country"]

percentage_mar = df["permar"]
percentage_apr = df["perapr"]
percentage_may = df["permay"]
percentage_jun = df["perjun"]
percentage_jul = df["perjul"]


tweet0 = []
tweet1 =[]
tweet2 =[]
tweet3 =[]

    
tweet0 = [percentage_mar[0],percentage_apr[0],percentage_may[0], percentage_jun[0], percentage_jul[0]] 
tweet1 = [percentage_mar[1],percentage_apr[1],percentage_may[1], percentage_jun[1], percentage_jul[1]]
tweet2 = [percentage_mar[2],percentage_apr[2],percentage_may[2], percentage_jun[2], percentage_jul[2]]
tweet3 = [percentage_mar[3],percentage_apr[3],percentage_may[3], percentage_jun[3], percentage_jul[3]]
months = range(1, 5)

plot(months, tweet0,months, tweet1, months, tweet2, months, tweet3,marker='+')

data = read_csv("FINALAUS1.csv")
topics = data['topic'].tolist()
legend(topics)
title('Australia data mapped over time (including hashtagged data)')
xlabel('Month')
ylabel('Number of tweets found')

show()