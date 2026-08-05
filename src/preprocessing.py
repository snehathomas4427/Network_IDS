#Remove duplicates, Handle NaNs, Handle infinite values, Encode labels, Normalize numerical columns
import pandas as pd
import numpy as np

from pathlib import Path
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def clean_data(df):

    # Remove whitespace from column names
    df.columns = df.columns.str.strip()

    # Replace infinite values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Fill missing Flow Bytes/s values
    df["Flow Bytes/s"] = df["Flow Bytes/s"].fillna(
        df["Flow Bytes/s"].median()
    )

    return df

