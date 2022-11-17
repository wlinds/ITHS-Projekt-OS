import pandas as pd
import os

class OlympicsData:
    def __init__(self, data_folder_path:str) -> None:
        self._data_folder_path = data_folder_path

    def _dataframe(self, stockname:str)->list:
        stock_df_list = []

        for path_ending in ["_TIME_SERIES_DAILY_ADJUSTED.csv", "_TIME_SERIES_INTRADAY_EXTENDED.csv",]:
            # Example:
            # data_floder: c:/Users/vinee/Documents/Github/Databehandling-Vineela-Nedunuri/Code-alongs/stockdata
            # stocname: AAPL
            # path_ending : _TIME_SERIES_DAILY_ADJUSTED.csv
            # resulting path : c:/Users/vinee/Documents/Github/Databehandling-Vineela-Nedunuri/Code-alongs/stockdata/AAPL_TIME_SERIES_DAILY_ADJUSTED.csv
            path = os.path.join(self._data_folder_path, stockname+path_ending)

            stock = pd.read_csv(path, index_col = 0, parse_dates = True)
            stock.index.rename("Date", inplace = True)

            stock_df_list.append(stock)
        return stock_df_list
# first data file
df = pd.read_csv("../Project/Data/athlete_events.csv", usecols=['Name', 'Age', 'Sex', 'Team', 'NOC','Games','Year','Sport','Medal'])
#df.head()

# second data file
df1 = pd.read_csv("../Project/Data/noc_regions.csv",usecols=['region', 'NOC']) #### NOC: National Olympic Committee
#df1.head() 

# merge both the files with corresconding columns
df_merge = df1.merge(df, on="NOC",how = "left")
df_merge.head()