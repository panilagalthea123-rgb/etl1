import pandas as pd
from database import engine
import os
from flask import Flask


print("Starting Final Load...")
df_j_clean = pd.read_sql('trf_japan', engine)
df_m_clean = pd.read_sql('trf_myanmar', engine)
df_final = pd.concat([df_j_clean, df_m_clean], ignore_index=True)
df_final.to_sql('fact_global_sales', engine, if_exists='replace', index=False)
print("ETL Process Complete.")


app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>ETL Pipeline Live</h1><p>The Python script has successfully executed in the cloud. Presentation layer is ready.</p>"

if __name__ == "__main__":
    # Render uses the 'PORT' environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
