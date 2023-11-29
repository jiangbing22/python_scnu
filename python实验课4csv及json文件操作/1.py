import pandas as pd
df = pd.read_json("beijing_aqi.json");
df_sorted=df.sort_values(by="pm2_5",ascending=True)
df_sorted.to_csv("test1.csv",index=False)