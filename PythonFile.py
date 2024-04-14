import numpy as np
import pandas as pd
import time
import logging


def readCsvFiles(path):
    df = pd.read_csv(path)
    return df

def selectCols(df, cols = []):
    df = df[col]
    return df






