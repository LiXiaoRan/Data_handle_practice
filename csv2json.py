import pandas as pd
import numpy as np

data = pd.read_csv('sum_data.csv')
df = pd.DataFrame(data=data)
print df[df['id'] == 0]
df[df['id'] == 0].to_json(orient='index',path_or_buf='sum_prjectV_data.json',force_ascii=False)
# df.to_json(orient='index',path_or_buf='sum_prjectV_data.json',force_ascii=False)
