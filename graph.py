from __future__ import annotations
from input import df_germany
import pandas as pd
import plotly.express as px




 # graph 1 is for age distribution
fig1 = px.histogram(df_germany, x='Age', color = 'Sex',  title= "Histogram of ages")


# graph 2 for total number if womens from Germany participated in olympics
df_female = df_germany.query("Sex == 'F'")
# for land statstics sort out the country :germany
#df_germany = df_medals[df_medals["region"] == "Germany"]
print(df_germany)

# What happened to the notes??? Did I remove them? /wil

=======
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
>>>>>>> main

