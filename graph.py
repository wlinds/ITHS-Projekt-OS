from __future__ import annotations
from input import *
import pandas as pd
import plotly.express as px


# Country participant age histogram
def age_gender_historgram():
    fig1 = px.histogram(
        df_germany, x="Age", color="Sex", title="Participant age histogram"
    )
    return fig1


# Country medal accumulation


def medal_graph():  #  graph 2 represents top 10 sports germany got medals
    df_medals = (
        pd.DataFrame(
            df_germany.groupby("Sport")["Medal"].count().sort_values(ascending=False)
        )
        .reset_index()
        .head(10)
    )
    fig2 = px.bar(
        df_medals,
        x="Sport",
        y="Medal",
        color="Sport",
        text_auto=True,
        labels={"Sport": "Sport", "value": "Number of medals"},
        title=f"Top 10 medals achieved in Germany",
    )
    fig2.update_xaxes(tickangle=45)
    return fig2


# Pie chart winter vs summer participation
def season_participation():
    seasons = df_germany["Season"].value_counts()
    return px.pie(
        df_germany,
        values=seasons,
        names=seasons.index[
            ::-1
        ],  # Reverse just for default color, change this if color scheme applied
        title="Winter & Summer Participation Ratio",
    )


## Femlaes participated in olympics
def female_participation():

    df_female = df_germany[["Year", "Sex", "Season"]]
    df_female = df_female[(df_female["Sex"] == "F")]
    # separte data frame created
    females = (
        df_female[["Year", "Season"]]
        .value_counts()
        .reset_index(name="count")
        .sort_values(by="Year", ascending=True)
    )

    fig3 = px.line(
        females,
        x="Year",
        y="count",
        color="Season",
        log_x=True,
        title=" Total number of females participated in Olympics",
    )
    fig3.update_xaxes(tickangle=45)
    return fig3


# graph for sport statstics


def sport_participation():
    df_sp = pd.DataFrame(
        df_merge.groupby(["Sport", "region"])[["Medal"]].value_counts()
    ).reset_index()
    sport = df_sp[df_sp["Sport"] == "Football"]
    fig = px.bar(
        sport,
        x="region",
        y=0,
        color="Medal",
        text_auto=True,
        labels={"Sport": "Sport", "0": "Number of medals"},
        title="Countries who won medals on Football",
    )
    return fig


# ------ Land statistics: ----- #

#### Top 10 medals in germany
# Barplot

### Age distubution
# Histogram

### # Top 10 in Germany  (Women in sports) # Women empowerment
# Subtitle # Female participating throughout history (Ger)


# ----- Sport statistics: ----- #

# Football (country/region)
# Dropdown -> Top Medals by country
#          -> Number of persons from country represented in sport
#          ->

# Athletics

# Cross country skiing
