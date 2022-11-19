from __future__ import annotations
import pandas as pd
from hash import hash_names

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

if __name__ == "__main__":

    # Testing below. This works for all countries. 
    path_a, path_b = "Data/athlete_events.csv", "Data/noc_regions.csv"
    usecols = ['Name', "Age", 'Sex', 'NOC', 'Games', 'Year', 'Sport', 'Medal']
    df = extract_data(path_a,path_b, usecols, hash=True, country_select="All")
    print(df.head())

    # This works if country_select="All"
    df_medal = df.groupby("Country")[["Medal"]].count().sort_values(by = "Medal",ascending= False).head(10).reset_index()
    print(df_medal.info)

    df = extract_data(path_a,path_b, usecols, hash=True, country_select="All")