import math
import os
import numpy as np
import pandas as pd

url = 'https://data.assemblee-nationale.fr/static/openData/repository/15/amo/deputes_actifs_csv_opendata/liste_deputes_libre_office.csv'

df=pd.read_csv(url)

print(df)