from __future__ import annotations
from input import df_germany
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



 # graph 1 is for age distribution
fig1 = px.histogram(df_germany, x='Age', color = 'Sex',  title= "Histogram of ages")



df_summer = df_germany.query("Sex == 'F' & Season == 'Summer'")
df_winter = df_germany.query("Sex == 'F' & Season == 'Winter'")

print(df_summer.head())
trace1 = go.scatter(x = df_summer["year"], y = df_summer["Total medals"], name = "Summer Games", 
    marker = dict(color = "Blue"), mode = "marker+lines")
trace2 = go.scatter(x = df_winter["year"], y = df_winter["Total medals"], name = "Winter Games", 
    marker = dict(color = "Orange"), mode = "marker+lines")
data = [trace1, trace2]
layout = dict(title = "Female Athlete in Germany", xaxis = dict(title = "Year"), yaxis =dict(title = "Number of medals"),
    hovermode = "closet" )

fig2 = dict(data= data, layout = layout)


# graph 2 for total number if womens from Germany participated in olympics
df_female = df_germany.query("Sex == 'F'")
# for land statstics sort out the country :germany
#df_germany = df_medals[df_medals["region"] == "Germany"]
print(df_germany)

# ------ Land statistics: ----- #

#### Top 10 medals in germany
# Barplot

### Age distubution
# Histogram

### # Top 10 in Germany  (Women in sports) # Women empowerment
#Subtitle # Female participating throughout history (Ger)



# ----- Sport statistics: ----- #

# Football (country/region)
# Dropdown -> Top Medals by country
#          -> Number of persons from country represented in sport
#          ->

# Athletics 

# Cross country skiing 


