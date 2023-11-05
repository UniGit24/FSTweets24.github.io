import plotly.express as px
import pandas as pd


# Import data from USGS
data = pd.read_csv('Data.csv')


# Drop rows with missing or invalid values in the 'severity' column
data = data.dropna(subset=['severity'])
data = data[data.severity >= 0]


# Create scatter map
fig = px.scatter_geo(data, lat='latitude', lon='longitude', color='severity', hover_name='place', title='Mapped Security Threats')
fig.show()
