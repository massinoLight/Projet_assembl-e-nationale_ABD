import json
import pandas as pd
with open('./data/liste_depute_histoirique.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)


print(df)



