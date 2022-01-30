import json
import pandas as pd
with open('./data/questions_au_gouvernement/QANR5L15QG11.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)


print(df)



