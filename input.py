from __future__ import annotations
import pandas as pd
import os

directory_path = os.path.dirname(__file__)
path = os.path.join(directory_path, "Data")

# create a class for path
class OlympicData:
    def __init__(self, data_folder_path:str) -> None:
        self._data_folder_path = data_folder_path
    
    def olympic_dataframe(self, olympicdata:str)->list: # create a function to read csv files
        """Join path of data folder and read csv files """

            # Example:
            # data_floder: c:/Users/vinee/Documents/Github/Databehandling-Vineela-Nedunuri/Code-alongs/odata
            # olympicname: athlete__events
            # resulting path : c:/Users/vinee/Documents/Github/Databehandling-Vineela-Nedunuri/Code-alongs/data/Aathlete__events.csv

        path = os.path.join(self._data_folder_path, olympicdata+".csv")
        olympic = pd.read_csv(path, index_col = None)
            
        return olympic

# Instantiate new object with data
olympicdata_object = OlympicData(path)

# load data
df = olympicdata_object.olympic_dataframe("athlete_events")
df1 = olympicdata_object.olympic_dataframe("noc_regions")

# Merge both files with NOC columns
df_merge = pd.merge(df, df1,  on="NOC",how = "left")

# Hashes Name column (pseudo-anonymisation)
#df_merge["Name"] = hash_column(df_merge)

# Get dummies to split the medals with separete column Bronze, Gold, Silver
df_medals = pd.concat([df_merge, pd.get_dummies(df["Medal"])], axis=1)

# Add Total medals column to dataframe
df_medals["Total medals"] = df_medals["Bronze"] + df_medals["Gold"]+ df_medals["Silver"]

# # for land statstics sort out the country :germany
df_germany = df_medals.query("region == 'Germany'")

# Create list with all regions
all_region = df_merge['region'].dropna().unique().tolist()

# Return any country as df
def get_region(df=df_merge, region=None):
    return df.loc[df['region'] == region]

# # for land statstics sort out the country :germany
df_germany = df_medals.query("region == 'Germany'")
print(df_germany)


# function to return a dataframe needed for xcs plots
def reusable_dataframe_xcs():
    # reading athlete_events as df1
    # df1 = pd.read_csv("../Data/athlete_events.csv")
    #df1.head()

    # reading noc_regions as df2, going to merge these
    # df2 = pd.read_csv("../Data/noc_regions.csv")
    #df2.head()
    #df1.head(1)

    # merging both files into one on NOC
    # df = pd.merge(df1, df2, on="NOC", how="left")
    # df.head(2)

    # cross country skiing only dataframe
    xcs_df = df_merge[df_merge["Sport"] == "Cross Country Skiing"]
    xcs_df.head()


    # dropping 'ID', 'Name', 'Age', 'Height', 'Weight' and NaN medals
    dropped_df = xcs_df.drop(columns=['ID','Name', 'Age', 'Height','Weight']).dropna(subset='Medal')

    # dropping duplicates to seperate team events
    # going to use 'reusable_df' as a basline dataframe
    reusable_df = dropped_df.drop_duplicates()
    return reusable_df