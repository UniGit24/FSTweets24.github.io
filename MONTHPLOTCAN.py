from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd
from pandas import *



df = pd.read_csv('FINALUS.csv')

topic_list = df["topic"]
countries = df["country"]
percentage_june = df["percentage june"]
percentage_july = df["percentage july"]
percentage_august = df["percentage august"]
percentage_september = df["percentage september"]
percentage_october = df["percentage october"]

tweet0 = []
tweet1 =[]
tweet2 =[]
tweet3 =[]
tweet4 =[]

    
#FIND AS A PERCENTAGE OF TOTAL TWEETS THE ONES ABOVE 80   
tweet0 = [percentage_june[0],percentage_july[0],percentage_august[0],percentage_september[0],percentage_october[0]] 
tweet1 = [percentage_june[1],percentage_july[1],percentage_august[1],percentage_september[1],percentage_october[1]]
tweet2 = [percentage_june[2],percentage_july[2],percentage_august[2],percentage_september[2],percentage_october[2]]
tweet3 = [percentage_june[3],percentage_july[3],percentage_august[3],percentage_september[3],percentage_october[3]]
tweet4 = [percentage_june[4],percentage_july[4],percentage_august[4],percentage_september[4],percentage_october[4]]
months = range(1, 6)

# Plot the line WITH dots and the LINE
plot(months, tweet0,months, tweet1, months, tweet2, months, tweet3,months, tweet4,months,marker='+')

data = read_csv("FINALUS.csv")
topics = data['topic'].tolist()
#legend(["August 9 - Victoria to enter sixth lockdown","26 June – Greater Sydney, Wollongong, Blue Mountains and the Central Coast are placed into lockdown as the Delta variant of COVID-19 spreads.", " 11 July – Australia records its first death from the COVID-19 pandemic for 2021,as Sydney records 77 cases of community transmission.", "16 July – Melbourne enters snap lockdown with 18 cases of COVID-19.", "21 August – New South Wales records the highest daily COVID-19 case numbers in Australia thus far, recording 825 new cases of COVID-19.","25 August – New South Wales records 1,029 new cases of COVID-19 in 24 hours becoming the first state in Australia to surpass the 1,000 daily case milestone."])
legend(topics)
# Apply the TITLE, X-axis and Y-axis label
title('USA data mapped over time')
xlabel('Month')
ylabel('Number of tweets found')

show()