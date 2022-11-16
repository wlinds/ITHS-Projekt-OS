import pandas as pd
# first data file
df = pd.read_csv("../Project/Data/athlete_events.csv", usecols=['Name', 'Age', 'Sex', 'Team', 'NOC','Games','Year','Sport','Medal'])
#df.head()

# second data file
df1 = pd.read_csv("../Project/Data/noc_regions.csv",usecols=['region', 'NOC']) #### NOC: National Olympic Committee
#df1.head() 

# merge both the files with corresconding columns
df_merge = df1.merge(df, on="NOC",how = "left")
df_merge.head()