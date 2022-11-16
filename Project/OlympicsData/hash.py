from __future__ import annotations
import pandas as pd
import hashlib
# first data file
df = pd.read_csv("../Project/OlympicsData/athlete_events.csv", usecols=['Name', 'Age', 'Sex', 'Team', 'NOC','Games','Year','Sport','Medal'])
df.head()

# second data file
df1 = pd.read_csv("../Project/OlympicsData/noc_regions.csv",usecols=['region', 'NOC']) #### NOC: National Olympic Committee
df1.head() 
# merge both the files with corresconding columns
df_merge = df1.merge(df, on="NOC",how = "left")
df_merge.head()



def hash_team(df_merge, country: str) -> pd.Series:
    """Returns column with hashed ahtlete names as pd.series."""

    # Might need some error and exception handling, this should convert to string and works for now:    
    #df_merge["region"] = df_merge["region"].astype(str)

    # Slice country parameter from DataFrame
    df_germany = df_merge[df_merge["region"] == country]

    # Lambda function for encoding, hashing and digest hex
    return df_germany.iloc[:,2].apply(
        lambda x: hashlib.sha256(x.encode()).hexdigest())

country = "Germany"

hash_team(df_merge, country)