import pandas as pd
from database import engine

print("Starting Final Load...")


df_j_clean = pd.read_sql('trf_japan', engine)
df_m_clean = pd.read_sql('trf_myanmar', engine)


df_final = pd.concat([df_j_clean, df_m_clean], ignore_index=True)


print("Uploading to Presentation layer (Master Table)...")
df_final.to_sql('fact_global_sales', engine, if_exists='replace', index=False)

print("Load Stage: Success! Your Master Table 'fact_global_sales' is ready.")