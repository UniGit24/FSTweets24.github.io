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
    #data = data[data.longitude >= 0]

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





root = Tk()              
root.geometry("750x150") 
btn = Button(root, text = 'Australia', command = showmap("Australia")) 
btn.place(x=325, y=50)
btn = Button(root, text = 'Brazil', command = showmap("Brazil")) 
btn.place(x=325, y=60)
btn = Button(root, text = 'Canada', command = showmap("Canada")) 
btn.place(x=325, y=70)
btn = Button(root, text = 'France', command = showmap("France")) 
btn.place(x=325, y=80)
btn = Button(root, text = 'Germany', command = showmap("Germany")) 
btn.place(x=325, y=90)
btn = Button(root, text = 'India', command = showmap("India")) 
btn.place(x=325, y=100)
btn = Button(root, text = 'Italy', command = showmap("Italy")) 
btn.place(x=325, y=110)
btn = Button(root, text = 'Mexico', command = showmap("Mexico")) 
btn.place(x=325, y=120)
btn = Button(root, text = 'Ukraine', command = showmap("Ukraine")) 
btn.place(x=325, y=130)
btn = Button(root, text = 'United States', command = showmap("United States")) 
btn.place(x=325, y=140)

#btn.pack(side = 'top')    
 
root.mainloop()
