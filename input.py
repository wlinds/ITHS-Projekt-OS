from __future__ import annotations
import pandas as pd
from hash import hash_names
import os

def extract_data(path_a: str,
        path_b:str,
        cols_select:list,
        hash: bool,
        country_select: str) -> pd.DataFrame:
    """Takes two paths, merges and hashes names (optional).
    Returns DataFrame with either a specific country or all countries.

    Attributes
    ----------
    cols_select : list
        Input list to get any of the following columns:
        'ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games',
       'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'

    hash : bool
        Hashes "Name" column if True.

    country_select: str
        Input country in string format.
        If set to "All" returns all countries.
    """
    # TODO: This needs exception and error handling!

    df = pd.read_csv(path_a,
        usecols=cols_select)
    df1 = pd.read_csv(path_b,
        usecols=['region', 'NOC'])

    # Calling hash.py, hashing names: 
    if hash: df["Name"] = hash_names(df, "Name")

    # Left outer join merge, -> combines historical arbitrary differences, eg. wars and political "games". NOC convention.
    df = df1.merge(df, on="NOC", how = "left")
    
    # Rename column region to Country
    df.rename(columns = {'region':'Country'}, inplace=True)

    # Returns either All countries or selected country
    if country_select == "All":
        return df
    else:
        return df.loc[df['Country'] == country_select]


# I think this is pretty neat. Of course we can do more, like add more function parameters or even make it a class or something. /wil

# create a class for path of data
class OlympicData:
    def __init__(self, data_folder_path:str) -> None:
        self._data_folder_path = data_folder_path
    
    def olympic_dataframe(self, olympicdata:str)->list: # create a function to read csv files

        """Create a function that joins the path of data folder and read csv files """

            # Example:
            # data_floder: c:/Users/vinee/Documents/Github/Databehandling-Vineela-Nedunuri/Code-alongs/odata
            # olympicname: athlete__events
            # resulting path : c:/Users/vinee/Documents/Github/Databehandling-Vineela-Nedunuri/Code-alongs/data/Aathlete__events.csv
        path = os.path.join(self._data_folder_path, olympicdata+".csv")
        olympic = pd.read_csv(path, index_col = None, parse_dates = True)
            
        return olympic
    

if __name__ == "__main__":

    # Testing below.

    directory_path = os.path.dirname(__file__)
    path = os.path.join(directory_path, "Data")

    print(path)

    olympicdata_object = OlympicData(path)

    # load data
    df = olympicdata_object.olympic_dataframe("athlete_events")
    df1 = olympicdata_object.olympic_dataframe("noc_regions")

    # merge both the files with corresconding columns
    df_merge = pd.merge(df, df1,  on="NOC",how = "left")
    #print(df_merge)

    #Create a new columns of medals of dataframe for easy analysis

    # Get dummies to split the medals with separete column Bronze, Gold, Silver
    df_medals = pd.concat([df_merge, pd.get_dummies(df["Medal"])], axis=1)

    # Add Total medals column to dataframe
    df_medals["Total medals"] = df_medals["Bronze"] + df_medals["Gold"]+ df_medals["Silver"] 
    print(df_medals.head())  