import math
import os
import numpy as np
import pandas as pd

url = 'https://data.assemblee-nationale.fr/static/openData/repository/CONSULTATIONS_CITOYENNES/HAINE_SUR_INTERNET/Haine-sur-Internet.csv'

df=pd.read_csv(url,encoding = "cp1252")

print(df.dtypes)

