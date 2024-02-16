from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd
from pandas import *



df = pd.read_csv('FINALCAN.csv')

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
tweet5 =[]
tweet6 =[]
tweet7 =[]
tweet8 =[]
tweet9 =[]
tweet10 =[]
tweet11 =[]
tweet12 =[]
tweet13 =[]
tweet14 =[]
tweet15 =[]
tweet16 =[]
tweet17 =[]
tweet18 =[]
tweet19 =[]
tweet20 =[]
tweet21 =[]
tweet22 =[]
    
#FIND AS A PERCENTAGE OF TOTAL TWEETS THE ONES ABOVE 80   
tweet0 = [percentage_june[0],percentage_july[0],percentage_august[0],percentage_september[0],percentage_october[0]] 
tweet1 = [percentage_june[1],percentage_july[1],percentage_august[1],percentage_september[1],percentage_october[1]]
tweet2 = [percentage_june[2],percentage_july[2],percentage_august[2],percentage_september[2],percentage_october[2]]
tweet3 = [percentage_june[3],percentage_july[3],percentage_august[3],percentage_september[3],percentage_october[3]]
tweet4 = [percentage_june[4],percentage_july[4],percentage_august[4],percentage_september[4],percentage_october[4]]
tweet5 = [percentage_june[5],percentage_july[5],percentage_august[5],percentage_september[5],percentage_october[5]]
tweet6 = [percentage_june[6],percentage_july[6],percentage_august[6],percentage_september[6],percentage_october[6]] 
tweet7 = [percentage_june[7],percentage_july[7],percentage_august[7],percentage_september[7],percentage_october[7]]
tweet8 = [percentage_june[8],percentage_july[8],percentage_august[8],percentage_september[8],percentage_october[8]]
tweet9 = [percentage_june[9],percentage_july[9],percentage_august[9],percentage_september[9],percentage_october[9]]
tweet10 = [percentage_june[10],percentage_july[10],percentage_august[10],percentage_september[10],percentage_october[10]]
tweet11 = [percentage_june[11],percentage_july[11],percentage_august[11],percentage_september[11],percentage_october[11]]
tweet12 = [percentage_june[12],percentage_july[12],percentage_august[12],percentage_september[12],percentage_october[12]] 
tweet13 = [percentage_june[13],percentage_july[13],percentage_august[13],percentage_september[13],percentage_october[13]]
tweet14 = [percentage_june[14],percentage_july[14],percentage_august[14],percentage_september[14],percentage_october[14]]
tweet15 = [percentage_june[15],percentage_july[15],percentage_august[15],percentage_september[15],percentage_october[15]]
tweet16 = [percentage_june[16],percentage_july[16],percentage_august[16],percentage_september[16],percentage_october[16]]
tweet17 = [percentage_june[17],percentage_july[17],percentage_august[17],percentage_september[17],percentage_october[17]]
tweet18 = [percentage_june[18],percentage_july[18],percentage_august[18],percentage_september[18],percentage_october[18]]
tweet19 = [percentage_june[19],percentage_july[19],percentage_august[19],percentage_september[19],percentage_october[19]]
tweet20 = [percentage_june[20],percentage_july[20],percentage_august[20],percentage_september[20],percentage_october[20]]
tweet21 = [percentage_june[21],percentage_july[21],percentage_august[21],percentage_september[21],percentage_october[21]]
tweet22 = [percentage_june[22],percentage_july[22],percentage_august[22],percentage_september[22],percentage_october[22]]

months = range(1, 6)

# Plot the line WITH dots and the LINE
plot(months, tweet0,months, tweet1, months, tweet2, months, tweet3,months, tweet4,months, tweet5,months, tweet6,months, tweet7,months, tweet8,months, tweet9,months, tweet10,months, tweet11,months, tweet12,months, tweet13,months, tweet14,months, tweet15,months, tweet16,months, tweet17,months, tweet18,months, tweet19,months, tweet20,months, tweet21,months, tweet22,marker='+')

data = read_csv("FINALCAN.csv")
topics = data['topic'].tolist()
#legend(["August 9 - Victoria to enter sixth lockdown","26 June – Greater Sydney, Wollongong, Blue Mountains and the Central Coast are placed into lockdown as the Delta variant of COVID-19 spreads.", " 11 July – Australia records its first death from the COVID-19 pandemic for 2021,as Sydney records 77 cases of community transmission.", "16 July – Melbourne enters snap lockdown with 18 cases of COVID-19.", "21 August – New South Wales records the highest daily COVID-19 case numbers in Australia thus far, recording 825 new cases of COVID-19.","25 August – New South Wales records 1,029 new cases of COVID-19 in 24 hours becoming the first state in Australia to surpass the 1,000 daily case milestone."])
legend(topics)
# Apply the TITLE, X-axis and Y-axis label
title('Canada data mapped over time')
xlabel('Month')
ylabel('Number of tweets found')

show()