from __future__ import annotations
import pandas as pd
import hashlib

def hash_column(df:pd.DataFrame, select_column: str="Name") -> pd.Series:
    """Returns series with hashed ahtlete names as pd.series.
    Attributes
    ----------
    df: pd.DataFrame
        Input dataframe.

    select_column: str
        Selects column to hash. Defaults to Name.

    """

    # not coverting to string because name is already a string
    # what if future input contains non-string values /wil

    # Lambda function for encoding, hashing and digest hex
    return df[select_column].apply(
        lambda x: hashlib.sha256(x.encode()).hexdigest())

if __name__ == "__main__":
    pass
