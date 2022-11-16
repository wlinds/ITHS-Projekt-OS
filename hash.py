from __future__ import annotations
import pandas as pd
import hashlib

def hash_team(df, country: str) -> pd.Series:
    """Hashes column as series, values must be strings."""

    # Might need some error and exception handling,
    # this should convert to string
    
    df["Team"] = df["Team"].astype(str)

    # Slice country parameter from DataFrame
    df_GER = df.loc[df["Team"] == country]

    # Labda function for hashing
    return df_GER.iloc[:,1].apply(
        lambda x: hashlib.sha256(x.encode()).hexdigest())

if __name__ == "__main__":

    df = pd.read_csv("Data/athlete_events.csv")

    country = "Germany"

    print(hash_team(df, "Germany"))

