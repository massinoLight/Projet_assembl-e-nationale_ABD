import math
import os
import numpy as np
import pandas as pd

url = 'https://data.assemblee-nationale.fr/static/openData/repository/CONSULTATIONS_CITOYENNES/IDENTITE_NUMERIQUE/identitenumerique.csv'

df=pd.read_csv(url,encoding = "cp1252")

print(df.dtypes)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df['Debat'])