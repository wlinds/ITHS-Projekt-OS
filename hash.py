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

def hash_names(df, select_column: str) -> pd.Series:
    """Returns series with hashed ahtlete names."""

    # Need exception and error handling for inputs
    df[select_column] = df[select_column].astype(str) # <- Makes sure column contain strings

    # Previously anonymized names from column 1 in df specified by argument "Team" or "Region", that's why we used iloc[:,1] to get Name
    # Now we pass entire df as argument and use "Name" as key to find athlete name column

    # Lambda function for encoding, hashing and digest hex TODO: Add salt
    return df[select_column].apply(
        lambda x: hashlib.sha256(x.encode()).hexdigest())

if __name__ == "__main__":
    # Testing, this can be removed
    df = pd.read_csv("Data/athlete_events.csv", usecols=['Name', 'Age', 'Sex', 'Team', 'NOC','Games','Year','Sport','Medal'])
    df1 = pd.read_csv("Data/noc_regions.csv",usecols=['region', 'NOC']) #### NOC: National Olympic Committee

    # replace column Name with all hashed names (not germany only)
    df1["Name"] = hash_names(df, "Name")

    # merge both the files with corresconding columns
    df_merge = df1.merge(df, on="NOC",how = "left")

    print(df1["Name"])
