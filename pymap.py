import plotly.express as px
import pandas as pd
from tkinter import *

def showmap():
    window = Toplevel(root)
    window.title("Map")
    
    fig = px.scatter_geo()
    main(fig)


def main(fig):
    # Import data
    data = pd.read_csv('August21Data.csv')

    # Drop rows with missing or invalid values in the 'longitude' column
    data = data.dropna(subset=['longitude'])
    data = data[data.longitude >= 0]

    # Create scatter map
    fig = px.scatter_geo(data, lat='latitude', lon='longitude', hover_name = 'searched_hashtag_country', hover_data = 'tweet_text', title='Mapped Security Threats')
    #fig = px.scatter_mapbox(data, lat="latitude", lon="longitude",color="severity", size="severity", color_continuous_scale=px.colors.cyclical.IceFire, size_max=20,zoom=12)
    fig.show()

# create a tkinter window
root = Tk()              
 
# Open window having dimension 1000x1000
root.geometry('1000x1000') 
 
# Create a Button
btn = Button(root, text = 'Show map', bd = '5', command = showmap) 
 
# Set the position of button on the top of window.   
btn.pack(side = 'top')    
 
root.mainloop()

