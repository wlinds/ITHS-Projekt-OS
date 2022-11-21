from __future__ import annotations
import pandas as pd
from hash import hash_column
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
df_merge["Name"] = hash_column(df_merge)

# Get dummies to split the medals with separete column Bronze, Gold, Silver
df_medals = pd.concat([df_merge, pd.get_dummies(df["Medal"])], axis=1)

# Add Total medals column to dataframe
df_medals["Total medals"] = df_medals["Bronze"] + df_medals["Gold"]+ df_medals["Silver"] 

if __name__ == "__main__":

    # Testing below.

    df = df_medals[df_medals["region"] == "Germany"]

    df_merge["Name"] = hash_column(df_merge)

    #Create a new columns of medals of dataframe for easy analysis

    # Get dummies to split the medals with separete column Bronze, Gold, Silver
    df_medals = pd.concat([df_merge, pd.get_dummies(df["Medal"])], axis=1)

    # Add Total medals column to dataframe
    df_medals["Total medals"] = df_medals["Bronze"] + df_medals["Gold"]+ df_medals["Silver"] 
    print(df_medals.head())
    
    print(df_medals)  

    # # for land statstics sort out the country :germany
    df_germany = df_medals.query("region == 'Germany'")
    print(df_germany)
