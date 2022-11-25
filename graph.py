from __future__ import annotations
from input import *
import pandas as pd
import plotly.express as px
from dash import html, dcc
import dash_bootstrap_components as dbc

# Country participant age histogram
def age_gender_historgram():
    fig1 = px.histogram(
        df_germany, x="Age", color="Sex", title="Participant age histogram"
    )
    return fig1


# Germany XCS medal distribution
def germany_xcs():
    df_germany_2 = df_germany[df_germany["Sport"] == "Cross Country Skiing"]
    fig13 = px.bar(
    df_germany_2,
    x="Year",
    y="Year",
    color="Medal",
    labels={"Sport": "Sport", "0": "medals", "region": "Country"},
    barmode="group",
    title="Total medals, Germany cross country skiing",
    #text_auto = True,
    color_discrete_sequence=[px.colors.qualitative.Dark2[7],px.colors.qualitative.Dark2[5],px.colors.qualitative.Dark2[6]]
)
    return fig13

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
        color_discrete_sequence=[px.colors.qualitative.Dark2[5],px.colors.qualitative.Dark2[7],px.colors.qualitative.Dark2[6]],
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


def men_team_xcs_plot():
    
    reusable_df = df_merge
    # taking 'Cross Country Skiing Men's 4 x 10 kilometres Relay' only to save in a dataframe
    
    df_men_relay = reusable_df[reusable_df["Event"] == "Cross Country Skiing Men's 4 x 10 kilometres Relay"]
    # grouping by event + region. new column '0', counts medals. 
    # going to rename this one after concat with other mens team event
    df_men_relay = df_men_relay.groupby(["Event", "region"])[["Medal"]].value_counts().to_frame().reset_index()
    
    # same as above but for xcs men's team sprint
    df_men_sprint = reusable_df[reusable_df["Event"] == "Cross Country Skiing Men's Team Sprint"]
    df_men_sprint = df_men_sprint.groupby(["Event", "region"])[["Medal"]].value_counts().to_frame().reset_index()

    # concating df_men_relay and df_men_sprint
    frames = [df_men_sprint, df_men_relay]
    concat_men_df = pd.concat(frames)

    # sorting medals to get a nicer plot
    concat_men_df = concat_men_df.rename({0:'Amount'}, axis=1)
    concat_men_df.Medal = pd.Categorical(concat_men_df.Medal,categories=['Bronze', 'Silver', 'Gold'])
    concat_men_df = concat_men_df.sort_values('Medal')


    fig10 = px.histogram(
        concat_men_df,
        x="region",
        y="Amount",
        color="Medal",
        labels={"Sport": "Sport", "0": "medals", "region": "Country"},
        barmode="group",
        title="Men's team cross country skiing medals",
        text_auto = True,
        color_discrete_sequence=[px.colors.qualitative.Dark2[6],px.colors.qualitative.Dark2[7],px.colors.qualitative.Dark2[5]]
        )
    return fig10

def women_team_xcs_plot():
    
    reusable_df = df_merge
    
    #reusable_df = df_merge(columns=['ID','Name', 'Age', 'Height','Weight']).dropna(subset='Medal')
    reusable_df.drop_duplicates()
    # 3x5 k relay
    df_women_relay = reusable_df[reusable_df["Event"] == "Cross Country Skiing Women's 3 x 5 kilometres Relay"]
    df_women_relay = df_women_relay.groupby(["Event", "region"])[["Medal"]].value_counts().to_frame().reset_index()
    df_women_relay.drop_duplicates()
    # 4x5 relay
    df_women_4x_relay = reusable_df[reusable_df["Event"] == "Cross Country Skiing Women's 3 x 5 kilometres Relay"]
    df_women_4x_relay = df_women_4x_relay.groupby(["Event", "region"])[["Medal"]].value_counts().to_frame().reset_index()

    # team sprint
    df_women_sprint = reusable_df[reusable_df["Event"] == "Cross Country Skiing Women's Team Sprint"]
    df_women_sprint = df_women_sprint.groupby(["Event", "region"])[["Medal"]].value_counts().to_frame().reset_index()

    # concating dfs into one, to plot it
    frames = [df_women_relay, df_women_4x_relay, df_women_sprint]
    concat_women_team = pd.concat(frames)
    #concat_women_team.drop_duplicates()
    # sorting medals to get a nicer plot + renaming axis
    concat_women_team = concat_women_team.rename({0:'Amount'}, axis=1)

    concat_women_team.Medal = pd.Categorical(concat_women_team.Medal,categories=['Bronze', 'Silver', 'Gold'])
    concat_women_team = concat_women_team.sort_values('Medal')

    # plotting
    fig11 = px.histogram(
    concat_women_team,
    x="region",
    y="Amount",
    color="Medal",
    labels={"Sport": "Sport", "0": "medals", "region": "Country"},
    barmode="group",
    title="Women's team cross country skiing medals by country",
    text_auto = True,
    color_discrete_sequence=[px.colors.qualitative.Dark2[6],px.colors.qualitative.Dark2[7],px.colors.qualitative.Dark2[5]]
    )
    return fig11

def total_individual_xcs_plot():

    reusable_df = df_merge[df_merge["Sport"] == "Cross Country Skiing"]

    # messy way to drop certain events
    total_individual_medals = reusable_df[reusable_df["Event"] != "Cross Country Skiing Men's Team Sprint"]

    total_individual_medals = total_individual_medals[total_individual_medals["Event"] != "Cross Country Skiing Women's Team Sprint"]

    total_individual_medals = total_individual_medals[total_individual_medals["Event"] != "Cross Country Skiing Women's 4 x 5 kilometres Relay"]

    total_individual_medals = total_individual_medals[total_individual_medals["Event"] != "Cross Country Skiing Women's 3 x 5 kilometres Relay"]

    total_individual_medals = total_individual_medals[total_individual_medals["Event"] != "Cross Country Skiing Men's 4 x 10 kilometres Relay"]

    # grouping the dataframe and counting medals
    total_individual_medals = total_individual_medals.groupby(["Event", "region"])[["Medal"]].value_counts().to_frame().reset_index()

    # sorting medals to get a nicer plot + renaming axis
    total_individual_medals = total_individual_medals.rename({0:'Amount'}, axis=1)

    total_individual_medals.Medal = pd.Categorical(total_individual_medals.Medal,categories=['Bronze', 'Silver', 'Gold'])
    total_individual_medals = total_individual_medals.sort_values('Medal')
    
    # plotting
    fig12 = px.histogram(
    total_individual_medals,
    x="region",
    y="Amount",
    color="Medal",
    labels={"Sport": "Sport", "0": "medals", "region": "Country"},
    barmode="group",
    title="Total individual medals by country",
    text_auto = True,
    color_discrete_sequence=[px.colors.qualitative.Dark2[6],px.colors.qualitative.Dark2[7],px.colors.qualitative.Dark2[5]]
)
    return fig12