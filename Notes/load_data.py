import pandas as pd
import os

# create a function to read data
class OlympicData:
    def __init__(self, data_folder_path:str) -> None:
        self._data_folder_path = data_folder_path
    
    def olympic_dataframe(self, olympicdata:str)->list:

            # Example:
            # data_floder: c:/Users/vinee/Documents/Github/Databehandling-Vineela-Nedunuri/Code-alongs/olympicdata
            # olympicname: athlete__events
            # resulting path : c:/Users/vinee/Documents/Github/Databehandling-Vineela-Nedunuri/Code-alongs/olympicdata/Aathlete__events.csv
            path = os.path.join(self._data_folder_path, olympicdata+".csv")
            

            olympic = pd.read_csv(path, index_col = None, parse_dates = True)
            
            return olympic
    


        

    