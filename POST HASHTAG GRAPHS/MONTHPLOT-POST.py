from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd
from pandas import *




df = pd.read_csv('FINALCAN2 copy.csv')

topic_list = df["topic"]
countries = df["country"]
percentage_jan = df["jan_percent"]
percentage_feb = df["feb_percent"]
percentage_mar = df["mar_percent"]
percentage_apr = df["apr_percent"]
percentage_may = df["may_percent"]
percentage_jun = df["june_percent"]
percentage_jul = df["july_percent"]


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

    
tweet0 = [percentage_jan[0],percentage_feb[0],percentage_mar[0],percentage_apr[0],percentage_may[0], percentage_jun[0], percentage_jul[0]] 
tweet1 = [percentage_jan[1],percentage_feb[1],percentage_mar[1],percentage_apr[1],percentage_may[1], percentage_jun[1], percentage_jul[1]]
tweet2 = [percentage_jan[2],percentage_feb[2],percentage_mar[2],percentage_apr[2],percentage_may[2], percentage_jun[2], percentage_jul[2]]
tweet3 = [percentage_jan[3],percentage_feb[3],percentage_mar[3],percentage_apr[3],percentage_may[3], percentage_jun[3], percentage_jul[3]]
tweet4 = [percentage_jan[4],percentage_feb[4],percentage_mar[4],percentage_apr[4],percentage_may[4], percentage_jun[4], percentage_jul[4]] 
tweet5 = [percentage_jan[5],percentage_feb[5],percentage_mar[5],percentage_apr[5],percentage_may[5], percentage_jun[5], percentage_jul[5]]
tweet6 = [percentage_jan[6],percentage_feb[6],percentage_mar[6],percentage_apr[6],percentage_may[6], percentage_jun[6], percentage_jul[6]]
tweet7 = [percentage_jan[7],percentage_feb[7],percentage_mar[7],percentage_apr[7],percentage_may[7], percentage_jun[7], percentage_jul[7]]
tweet8 = [percentage_jan[8],percentage_feb[8],percentage_mar[8],percentage_apr[8],percentage_may[8], percentage_jun[8], percentage_jul[8]] 
tweet9 = [percentage_jan[9],percentage_feb[9],percentage_mar[9],percentage_apr[9],percentage_may[9], percentage_jun[9], percentage_jul[9]]
tweet10 = [percentage_jan[10],percentage_feb[10],percentage_mar[10],percentage_apr[10],percentage_may[10], percentage_jun[10], percentage_jul[10]]
tweet11 = [percentage_jan[11],percentage_feb[11],percentage_mar[11],percentage_apr[11],percentage_may[11], percentage_jun[11], percentage_jul[11]]
tweet12 = [percentage_jan[12],percentage_feb[12],percentage_mar[12],percentage_apr[12],percentage_may[12], percentage_jun[12], percentage_jul[12]] 
tweet13 = [percentage_jan[13],percentage_feb[13],percentage_mar[13],percentage_apr[13],percentage_may[13], percentage_jun[13], percentage_jul[13]]
tweet14 = [percentage_jan[14],percentage_feb[14],percentage_mar[14],percentage_apr[14],percentage_may[14], percentage_jun[14], percentage_jul[14]]
tweet15 = [percentage_jan[15],percentage_feb[15],percentage_mar[15],percentage_apr[15],percentage_may[15], percentage_jun[15], percentage_jul[15]] 

months = range(1, 8)

plot(months, tweet0,months, tweet1, months, tweet2, months, tweet3,months, tweet4,months, tweet5,months, tweet6,months, tweet7,months, tweet8,months, tweet9,months, tweet10,months, tweet11,months, tweet12,months, tweet13,months, tweet14,months, tweet15,months, marker='+')
data = read_csv("FINALCAN2 copy.csv")
topics = data['topic'].tolist()
legend(topics)
title('Canada data mapped over time (including hashtagged data)')
xlabel('Month')
ylabel('Number of tweets found')

show()



df = pd.read_csv('FINALUS1 copy.csv')

topic_list = df["topic"]
countries = df["country"]
percentage_jan = df["jan_percent"]
percentage_feb = df["feb_percent"]
percentage_mar = df["mar_percent"]
percentage_apr = df["apr_percent"]
percentage_may = df["may_percent"]
percentage_jun = df["june_percent"]
percentage_jul = df["july_percent"]


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

    
tweet0 = [percentage_jan[0],percentage_feb[0],percentage_mar[0],percentage_apr[0],percentage_may[0], percentage_jun[0], percentage_jul[0]] 
tweet1 = [percentage_jan[1],percentage_feb[1],percentage_mar[1],percentage_apr[1],percentage_may[1], percentage_jun[1], percentage_jul[1]]
tweet2 = [percentage_jan[2],percentage_feb[2],percentage_mar[2],percentage_apr[2],percentage_may[2], percentage_jun[2], percentage_jul[2]]
tweet3 = [percentage_jan[3],percentage_feb[3],percentage_mar[3],percentage_apr[3],percentage_may[3], percentage_jun[3], percentage_jul[3]]
tweet4 = [percentage_jan[4],percentage_feb[4],percentage_mar[4],percentage_apr[4],percentage_may[4], percentage_jun[4], percentage_jul[4]] 
tweet5 = [percentage_jan[5],percentage_feb[5],percentage_mar[5],percentage_apr[5],percentage_may[5], percentage_jun[5], percentage_jul[5]]
tweet6 = [percentage_jan[6],percentage_feb[6],percentage_mar[6],percentage_apr[6],percentage_may[6], percentage_jun[6], percentage_jul[6]]
tweet7 = [percentage_jan[7],percentage_feb[7],percentage_mar[7],percentage_apr[7],percentage_may[7], percentage_jun[7], percentage_jul[7]]
tweet8 = [percentage_jan[8],percentage_feb[8],percentage_mar[8],percentage_apr[8],percentage_may[8], percentage_jun[8], percentage_jul[8]] 
tweet9 = [percentage_jan[9],percentage_feb[9],percentage_mar[9],percentage_apr[9],percentage_may[9], percentage_jun[9], percentage_jul[9]]
tweet10 = [percentage_jan[10],percentage_feb[10],percentage_mar[10],percentage_apr[10],percentage_may[10], percentage_jun[10], percentage_jul[10]]
tweet11 = [percentage_jan[11],percentage_feb[11],percentage_mar[11],percentage_apr[11],percentage_may[11], percentage_jun[11], percentage_jul[11]]
tweet12 = [percentage_jan[12],percentage_feb[12],percentage_mar[12],percentage_apr[12],percentage_may[12], percentage_jun[12], percentage_jul[12]] 
tweet13 = [percentage_jan[13],percentage_feb[13],percentage_mar[13],percentage_apr[13],percentage_may[13], percentage_jun[13], percentage_jul[13]]
tweet14 = [percentage_jan[14],percentage_feb[14],percentage_mar[14],percentage_apr[14],percentage_may[14], percentage_jun[14], percentage_jul[14]]
tweet15 = [percentage_jan[15],percentage_feb[15],percentage_mar[15],percentage_apr[15],percentage_may[15], percentage_jun[15], percentage_jul[15]] 
tweet16 = [percentage_jan[16],percentage_feb[16],percentage_mar[16],percentage_apr[16],percentage_may[16], percentage_jun[16], percentage_jul[16]]
tweet17 = [percentage_jan[17],percentage_feb[17],percentage_mar[17],percentage_apr[17],percentage_may[17], percentage_jun[17], percentage_jul[17]]
tweet18 = [percentage_jan[18],percentage_feb[18],percentage_mar[18],percentage_apr[18],percentage_may[18], percentage_jun[18], percentage_jul[18]] 
tweet19 = [percentage_jan[19],percentage_feb[19],percentage_mar[19],percentage_apr[19],percentage_may[19], percentage_jun[19], percentage_jul[19]]
tweet20 = [percentage_jan[20],percentage_feb[20],percentage_mar[20],percentage_apr[20],percentage_may[20], percentage_jun[20], percentage_jul[20]]
tweet21 = [percentage_jan[21],percentage_feb[21],percentage_mar[21],percentage_apr[21],percentage_may[21], percentage_jun[21], percentage_jul[21]] 
months = range(1, 8)

plot(months, tweet0,months, tweet1, months, tweet2, months, tweet3,months, tweet4,months, tweet5,months, tweet6,months, tweet7,months, tweet8,months, tweet9,months, tweet10,months, tweet11,months, tweet12,months, tweet13,months, tweet14,months, tweet15,months, tweet16,months, tweet17,months, tweet18,months, tweet19,months, tweet20,months, tweet21,months, marker='+')

data = read_csv("FINALUS1 copy.csv")
topics = data['topic'].tolist()
legend(topics)
title('US data mapped over time (including hashtagged data)')
xlabel('Month')
ylabel('Number of tweets found')

show()


df = pd.read_csv('FINALAUS2 copy.csv')

topic_list = df["topic"]
countries = df["country"]
percentage_jan = df["jan_percent"]
percentage_feb = df["feb_percent"]
percentage_mar = df["mar_percent"]
percentage_apr = df["apr_percent"]
percentage_may = df["may_percent"]
percentage_jun = df["june_percent"]
percentage_jul = df["july_percent"]


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

    
tweet0 = [percentage_jan[0],percentage_feb[0],percentage_mar[0],percentage_apr[0],percentage_may[0], percentage_jun[0], percentage_jul[0]] 
tweet1 = [percentage_jan[1],percentage_feb[1],percentage_mar[1],percentage_apr[1],percentage_may[1], percentage_jun[1], percentage_jul[1]]
tweet2 = [percentage_jan[2],percentage_feb[2],percentage_mar[2],percentage_apr[2],percentage_may[2], percentage_jun[2], percentage_jul[2]]
tweet3 = [percentage_jan[3],percentage_feb[3],percentage_mar[3],percentage_apr[3],percentage_may[3], percentage_jun[3], percentage_jul[3]]
tweet4 = [percentage_jan[4],percentage_feb[4],percentage_mar[4],percentage_apr[4],percentage_may[4], percentage_jun[4], percentage_jul[4]] 
tweet5 = [percentage_jan[5],percentage_feb[5],percentage_mar[5],percentage_apr[5],percentage_may[5], percentage_jun[5], percentage_jul[5]]
tweet6 = [percentage_jan[6],percentage_feb[6],percentage_mar[6],percentage_apr[6],percentage_may[6], percentage_jun[6], percentage_jul[6]]
tweet7 = [percentage_jan[7],percentage_feb[7],percentage_mar[7],percentage_apr[7],percentage_may[7], percentage_jun[7], percentage_jul[7]]
tweet8 = [percentage_jan[8],percentage_feb[8],percentage_mar[8],percentage_apr[8],percentage_may[8], percentage_jun[8], percentage_jul[8]] 
tweet9 = [percentage_jan[9],percentage_feb[9],percentage_mar[9],percentage_apr[9],percentage_may[9], percentage_jun[9], percentage_jul[9]]
tweet10 = [percentage_jan[10],percentage_feb[10],percentage_mar[10],percentage_apr[10],percentage_may[10], percentage_jun[10], percentage_jul[10]]
tweet11 = [percentage_jan[11],percentage_feb[11],percentage_mar[11],percentage_apr[11],percentage_may[11], percentage_jun[11], percentage_jul[11]]
tweet12 = [percentage_jan[12],percentage_feb[12],percentage_mar[12],percentage_apr[12],percentage_may[12], percentage_jun[12], percentage_jul[12]] 

months = range(1, 8)

plot(months, tweet0,months, tweet1, months, tweet2, months, tweet3,months, tweet4,months, tweet5,months, tweet6,months, tweet7,months, tweet8,months, tweet9,months, tweet10,months, tweet11,months, tweet12,months,months,marker='+')

data = read_csv("FINALAUS2 copy.csv")
topics = data['topic'].tolist()
legend(topics)
title('Australia data mapped over time (including hashtagged data)')
xlabel('Month')
ylabel('Number of tweets found')

show()
