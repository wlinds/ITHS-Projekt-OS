from __future__ import annotations
from input import df_germany
import pandas as pd
import plotly.express as px




 # graph 1 is for age distribution
fig1 = px.histogram(df_germany, x='Age', color = 'Sex',  title= "Histogram of ages")


# graph 2 for total number if womens from Germany participated in olympics
df_female = df_germany.query("Sex == 'F'")