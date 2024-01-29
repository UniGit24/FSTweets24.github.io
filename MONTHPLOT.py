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
        plot(months, tweet1, months, tweet2, months, tweet3,months, tweet4,months, tweet5,months, tweet6, marker='+')
        # Apply the legend to tell the graphs apart
        legend(["Victoria to enter sixth lockdown","26 June – Greater Sydney, Wollongong, Blue Mountains and the Central Coast are placed into lockdown as the Delta variant of COVID-19 spreads.", " 11 July – Australia records its first death from the COVID-19 pandemic for 2021,as Sydney records 77 cases of community transmission.", "16 July – Melbourne enters snap lockdown with 18 cases of COVID-19.", "21 August – New South Wales records the highest daily COVID-19 case numbers in Australia thus far, recording 825 new cases of COVID-19.","25 August – New South Wales records 1,029 new cases of COVID-19 in 24 hours becoming the first state in Australia to surpass the 1,000 daily case milestone."])

        # Apply the TITLE, X-axis and Y-axis label
        title('Australia data mapped over time')
        xlabel('Month')
        ylabel('Number of tweets found')

        show()

    if countries[index] == "United States":
        #FIND AS A PERCENTAGE OF TOTAL TWEETS THE ONES ABOVE 80    
        tweet1 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet2 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet3 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet4 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet5 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet6 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet7 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]

        months = range(1, 6)

        # Plot the line WITH dots and the LINE
        plot(months, tweet1, months, tweet2, months, tweet3,months, tweet4,months, tweet5,months, tweet6,months, tweet7, marker='+')
        # Apply the legend to tell the graphs apart
        legend(["June 1 - SARS-CoV-2 Delta variant becomes the dominant strain of COVID-19 in the United States", "June 1 - COVID-19 vaccines – Moderna seeks full approval from the FDA for the Moderna COVID-19 vaccine", "June 5 – Aftermath of the January 6 United States Capitol attack – The Department of Justice says that over 465 people have been arrested since the January 6 attack. It is also seeking information on 250 other suspects.", "July 20 - Tom Barrack, founder of Colony Capital and an advisor of Donald Trump, is indicted for making false statements to the FBI and being an unregistered agent for the United Arab Emirates.", "August 2 - COVID-19 vaccination: Over 70% of adults are reported to have received at least one dose of a COVID-19 vaccine.", "August 10 - New York Governor Andrew Cuomo announces he will resign effective August 24 after an inquiry found he sexually harassed multiple women.", "August 29 - Hurricane Ida makes landfall at 11:55am CDT near Port Fourchon, Louisiana, on the 16th anniversary of Hurricane Katrina."])

        # Apply the TITLE, X-axis and Y-axis label
        title('US data mapped over time')
        xlabel('Month')
        ylabel('Number of tweets found')

        show()
    if countries[index] == "Canada":
        #FIND AS A PERCENTAGE OF TOTAL TWEETS THE ONES ABOVE 80    
        tweet1 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet2 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet3 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]
        tweet4 = [percentage_june[index],percentage_july[index],percentage_august[index],percentage_september[index],percentage_october[index]]

        months = range(1, 6)

        # Plot the line WITH dots and the LINE
        plot(months, tweet1, months, tweet2, months, tweet3,months, tweet4, marker='+')
        # Apply the legend to tell the graphs apart
        legend(["June 21 – The Government of Canada announces the first phase to easing the COVID-19 border measures for travellers, thus lifting quarantine requirements for fully immunised travellers starting on July 5", "June 30 - Dozens of people have died amid an unprecedented heatwave that has smashed temperature records.", "July 20 – British Columbia declares a state of emergency in response to the 2021 British Columbia wildfires.", "August 2 -  SARS-CoV-2 Delta variant becomes the pre-dominant strain of COVID-19 in Canada."])
        # Apply the TITLE, X-axis and Y-axis label
        title('Canada data mapped over time')
        xlabel('Month')
        ylabel('Number of tweets found')

        show()