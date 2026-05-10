import pandas as pd
from database import engine

print("Starting Extraction...")


# Make sure you renamed the sales_data.csv files to these names!
df_japan = pd.read_csv('data/japan_store.csv')
df_myanmar = pd.read_csv('data/myanmar_store.csv')


print("Uploading to Render...")
df_japan.to_sql('stg_japan', engine, if_exists='replace', index=False)
df_myanmar.to_sql('stg_myanmar', engine, if_exists='replace', index=False)

print("Extract Stage: Success! Tables 'stg_japan' and 'stg_myanmar' created.")