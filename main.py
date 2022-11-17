import pandas as pd
from hash import hash_region
import dash


# testing

# first data file
df = pd.read_csv("Data/athlete_events.csv", usecols=['Name', 'Age', 'Sex', 'Team', 'NOC','Games','Year','Sport','Medal'])
df.head()
# second data file
df1 = pd.read_csv("Data/noc_regions.csv",usecols=['region', 'NOC']) #### NOC: National Olympic Committee
df1.head() 
# merge both the files with corresconding columns
df_merge = df1.merge(df, on="NOC",how = "left")

country = "Germany"
hashed_series = hash_region(df_merge, country) # Replace columns
print(hashed_series.head())

if __name__ == "__main__":
    app.run