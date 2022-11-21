from __future__ import annotations
from input import df_medals
import pandas as pd


# for land statstics sort out the country :germany
df_germany = df_medals[df_medals["region"] == "Germany"]
print(df_germany)

# What happened to the notes??? Did I remove them? /wil