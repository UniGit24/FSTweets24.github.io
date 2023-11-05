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
    data = pd.read_csv('Data.csv')

    # Drop rows with missing or invalid values in the 'severity' column
    data = data.dropna(subset=['severity'])
    data = data[data.severity >= 0]

    # Create scatter map
    fig = px.scatter_geo(data, lat='latitude', lon='longitude', color='severity', hover_name='place', title='Mapped Security Threats')
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

