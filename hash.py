from __future__ import annotations
import pandas as pd
import hashlib

def hash_region(df_merge, country: str) -> pd.Series:
    """Returns column with hashed ahtlete names as pd.series."""

    #df_merge["region"] = df_merge["region"].astype(str)

    # Slice country parameter from DataFrame
    df_germany = df_merge[df_merge["region"] == country]

    # Lambda function for encoding, hashing and digest hex
    return df_germany.iloc[:,2].apply(
        lambda x: hashlib.sha256(x.encode()).hexdigest())


if __name__ == "__main__":
    # first data file
    df = pd.read_csv("Data/athlete_events.csv", usecols=['Name', 'Age', 'Sex', 'Team', 'NOC','Games','Year','Sport','Medal'])
    df.head()

    # second data file
    df1 = pd.read_csv("Data/noc_regions.csv",usecols=['region', 'NOC']) #### NOC: National Olympic Committee
    df1.head() 
    # merge both the files with corresconding columns
    df_merge = df1.merge(df, on="NOC",how = "left")
    df_merge.head()


    country = "Iceland" # test lol

    hashed_series = hash_region(df_merge, country) # Replace columns

    print(hashed_series.head())