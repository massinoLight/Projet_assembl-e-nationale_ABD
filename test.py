import json
import pandas as pd
with open('./data/PA235.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)


print(df)



