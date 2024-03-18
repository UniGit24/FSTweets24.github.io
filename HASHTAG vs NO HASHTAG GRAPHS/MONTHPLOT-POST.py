from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd
from pandas import *




df = pd.read_csv('FINALAUS2.csv')

percentage_jan = df["jan"]
percentage_feb = df["feb"]
percentage_mar = df["mar"]
percentage_apr = df["apr"]
percentage_may = df["may"]
percentage_jun = df["jun"]
h_jan = df["jan_h"]
h_feb = df["feb_h"]
h_mar = df["mar_h"]
h_apr = df["apr_h"]
h_may = df["may_h"]
h_jun = df["jun_h"]


tweet0 = []
tweet1 =[]



    
tweet0 = [percentage_jan[0] - h_jan[0],percentage_feb[0] - h_feb[0],percentage_mar[0]- h_mar[0],percentage_apr[0]- h_apr[0],percentage_may[0]- h_may[0], percentage_jun[0]- h_jun[0]] 
tweet1 = [h_jan[0],h_feb[0],h_mar[0],h_apr[0],h_may[0], h_jun[0]] 



months = range(1, 7)

plot(months, tweet0,months, tweet1,marker='+')
topics = ["non-hashatag number", "hashtag number"]
legend(topics)
title('Hashtags vs no hashtag Graph 1')
xlabel('Month')
ylabel('Number of tweets found')

show()


from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd
from pandas import *




df = pd.read_csv('FINALAUS2.csv')

percentage_jan = df["jan"]
percentage_feb = df["feb"]
percentage_mar = df["mar"]
percentage_apr = df["apr"]
percentage_may = df["may"]
percentage_jun = df["jun"]
h_jan = df["jan_h"]
h_feb = df["feb_h"]
h_mar = df["mar_h"]
h_apr = df["apr_h"]
h_may = df["may_h"]
h_jun = df["jun_h"]


tweet0 = []
tweet1 =[]



    
tweet0 = [percentage_jan[1] - h_jan[1],percentage_feb[1] - h_feb[1],percentage_mar[1]- h_mar[1],percentage_apr[1]- h_apr[1],percentage_may[1]- h_may[1], percentage_jun[1]- h_jun[1]] 
tweet1 = [h_jan[1],h_feb[1],h_mar[1],h_apr[1],h_may[1], h_jun[1]] 



months = range(1, 7)

plot(months, tweet0,months, tweet1,marker='+')
topics = ["non-hashatag number", "hashtag number"]
legend(topics)
title('Hashtags vs no hashtag Graph 2')
xlabel('Month')
ylabel('Number of tweets found')

show()


from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd
from pandas import *




df = pd.read_csv('FINALAUS2.csv')

percentage_jan = df["jan"]
percentage_feb = df["feb"]
percentage_mar = df["mar"]
percentage_apr = df["apr"]
percentage_may = df["may"]
percentage_jun = df["jun"]
h_jan = df["jan_h"]
h_feb = df["feb_h"]
h_mar = df["mar_h"]
h_apr = df["apr_h"]
h_may = df["may_h"]
h_jun = df["jun_h"]


tweet0 = []
tweet1 =[]



    
tweet0 = [percentage_jan[2] - h_jan[2],percentage_feb[2] - h_feb[2],percentage_mar[2]- h_mar[2],percentage_apr[2]- h_apr[2],percentage_may[2]- h_may[2], percentage_jun[2]- h_jun[2]] 
tweet1 = [h_jan[2],h_feb[2],h_mar[2],h_apr[2],h_may[2], h_jun[2]] 



months = range(1, 7)

plot(months, tweet0,months, tweet1,marker='+')
topics = ["non-hashatag number", "hashtag number"]
legend(topics)
title('Hashtags vs no hashtag Graph 3')
xlabel('Month')
ylabel('Number of tweets found')

show()
