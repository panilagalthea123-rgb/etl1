import pandas as pd
from database import engine

print("Starting Transformation...")


df_j = pd.read_sql('stg_japan', engine)
df_m = pd.read_sql('stg_myanmar', engine)


df_j.columns = [c.replace("'", "") for c in df_j.columns]
df_m.columns = [c.replace("'", "") for c in df_m.columns]


df_j = df_j.dropna()
df_m = df_m.dropna()


df_j['price_usd'] = pd.to_numeric(df_j['quantity']) * 0.0066 
df_m['price_usd'] = pd.to_numeric(df_m['quantity'])


print("Uploading to Transformation layer...")
df_j.to_sql('trf_japan', engine, if_exists='replace', index=False)
df_m.to_sql('trf_myanmar', engine, if_exists='replace', index=False)

print("Transform Stage: Success! Quotes removed and data cleaned.")