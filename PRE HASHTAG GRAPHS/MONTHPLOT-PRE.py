from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd
from pandas import *



df = pd.read_csv('FINALAUS1.csv')

topic_list = df["topic"]
countries = df["country"]
percentage_jan = df["perjan"]
percentage_feb = df["perfeb"]
percentage_mar = df["permar"]
percentage_apr = df["perapr"]
percentage_may = df["permay"]
percentage_jun = df["perjun"]
percentage_jul = df["perjul"]


tweet0 = []
tweet1 =[]
tweet2 =[]
tweet3 =[]
#tweet4 =[]

    
#FIND AS A PERCENTAGE OF TOTAL TWEETS THE ONES ABOVE 80   
tweet0 = [percentage_jan[0],percentage_feb[0],percentage_mar[0],percentage_apr[0],percentage_may[0], percentage_jun[0], percentage_jul[0]] 
tweet1 = [percentage_jan[1],percentage_feb[1],percentage_mar[1],percentage_apr[1],percentage_may[1], percentage_jun[1], percentage_jul[1]]
tweet2 = [percentage_jan[2],percentage_feb[2],percentage_mar[2],percentage_apr[2],percentage_may[2], percentage_jun[2], percentage_jul[2]]
tweet3 = [percentage_jan[3],percentage_feb[3],percentage_mar[3],percentage_apr[3],percentage_may[3], percentage_jun[3], percentage_jul[3]]
#tweet4 = [percentage_june[4],percentage_july[4],percentage_august[4],percentage_september[4],percentage_october[4]]
months = range(1, 8)

# Plot the line WITH dots and the LINE
plot(months, tweet0,months, tweet1, months, tweet2, months, tweet3,marker='+')

data = read_csv("FINALAUS1.csv")
topics = data['topic'].tolist()
#legend(["August 9 - Victoria to enter sixth lockdown","26 June – Greater Sydney, Wollongong, Blue Mountains and the Central Coast are placed into lockdown as the Delta variant of COVID-19 spreads.", " 11 July – Australia records its first death from the COVID-19 pandemic for 2021,as Sydney records 77 cases of community transmission.", "16 July – Melbourne enters snap lockdown with 18 cases of COVID-19.", "21 August – New South Wales records the highest daily COVID-19 case numbers in Australia thus far, recording 825 new cases of COVID-19.","25 August – New South Wales records 1,029 new cases of COVID-19 in 24 hours becoming the first state in Australia to surpass the 1,000 daily case milestone."])
legend(topics)
# Apply the TITLE, X-axis and Y-axis label
title('Australia data mapped over time (including hashtagged data)')
xlabel('Month')
ylabel('Number of tweets found')

show()