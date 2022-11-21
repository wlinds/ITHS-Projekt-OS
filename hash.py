from __future__ import annotations
import pandas as pd
import hashlib
from input import df_germany



def hash_team(df_germany, select_column: str) -> pd.Series:
    """Returns column with hashed ahtlete names as pd.series."""

    # not coverting to string because name is already a string

    # Lambda function for encoding, hashing and digest hex
    return df_germany[select_column].apply(
        lambda x: hashlib.sha256(x.encode()).hexdigest())

select_column = "Name"

print(hash_team(df_germany, select_column))

