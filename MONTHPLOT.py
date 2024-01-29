from pylab import plot, show, title, xlabel, ylabel
from pylab import legend
from pylab import axis
import pandas as pd


df = pd.read_csv('FINAL_RESULTS.csv')

topic_list = df["topic"]
countries = df["country"]
percentage_june = df["percentage june"]
percentage_july = df["percentage july"]
percentage_august = df["percentage august"]
percentage_september = df["percentage september"]
percentage_october = df["percentage october"]

for index, x in enumerate(topic_list, start=1): 
    if countries[index] == "Australia":
        #FIND AS A PERCENTAGE OF TOTAL TWEETS THE ONES ABOVE 80    
        tweet1 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet2 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet3 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet4 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet5 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet6 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]

        months = range(1, 6)

        # Plot the line WITH dots and the LINE
        plot(months, tweet1, months, tweet2, months, tweet3, marker='+')
        # Apply the legend to tell the graphs apart
        legend(["Victoria to enter sixth lockdown","26 June – Greater Sydney, Wollongong, Blue Mountains and the Central Coast are placed into lockdown as the Delta variant of COVID-19 spreads.", " 11 July – Australia records its first death from the COVID-19 pandemic for 2021,as Sydney records 77 cases of community transmission.", "16 July – Melbourne enters snap lockdown with 18 cases of COVID-19.", "21 August – New South Wales records the highest daily COVID-19 case numbers in Australia thus far, recording 825 new cases of COVID-19.","25 August – New South Wales records 1,029 new cases of COVID-19 in 24 hours becoming the first state in Australia to surpass the 1,000 daily case milestone."])

        # Apply the TITLE, X-axis and Y-axis label
        title('Australia data mapped over time')
        xlabel('Month')
        ylabel('Number of tweets found')

        show()