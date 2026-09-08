!pip install -q pdfplumber
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pdfplumber
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Setting visual style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Extracting data
pdf_path = '/content/vois input 3.pdf'
try:
    data_rows = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table: data_rows.extend(table)

    if data_rows:
        # Clean headers specifically to handle PDF artifacts
        headers = [str(c).strip().replace('\n', ' ') for c in data_rows[0]]
        df = pd.DataFrame(data_rows[1:], columns=headers)

        # Standardize malformed column names from PDF extraction
        rename_map = {
            'Farm_Area_Hec': 'Farm_Area_Hectares',
            'Avg_Temperatur': 'Avg_Temperature',
            'Sunlight_Hours_': 'Sunlight_Hours',
            'Soil_Moisture_p': 'Soil_Moisture_pct',
            'c Nitrogen_kg_ha': 'Nitrogen_kg_ha',
            'Phosphorus_kg_': 'Phosphorus_kg_ha',
            'Potassium_kg_h': 'Potassium_kg_ha',
            'Irrigation_Metho': 'Irrigation_Method',
            'Pesticide_Litre_': 'Pesticide_Litre_ha',
            'h Seed_Quality_S': 'Seed_Quality_Score',
            'c Yield_Tonnes_H': 'Yield_Tonnes_Ha',
            'Production_Tonn': 'Production_Tonnes',
            'Market_Price_IN': 'Market_Price_INR'
        }
        df = df.rename(columns=rename_map)

        # Aggressive cleaning of column names and dropping artifacts
        df.columns = [str(c).strip() for c in df.columns]
        if 'None' in df.columns:
            df = df.drop(columns=['None'])

        # Remove any leading/trailing characters from data values and convert to numeric
        numeric_cols = [
            'Farm_Area_Hectares', 'Rainfall_mm', 'Avg_Temperature', 'Humidity_pct',
            'Sunlight_Hours', 'Soil_pH', 'Soil_Moisture_pct', 'Nitrogen_kg_ha',
            'Phosphorus_kg_ha', 'Potassium_kg_ha', 'Fertilizer_kg_ha',
            'Pesticide_Litre_ha', 'Seed_Quality_Score', 'Water_Used_m3',
            'Water_Efficiency', 'Yield_Tonnes_Ha', 'Production_Tonnes',
            'Market_Price_INR', 'Total_Cost_INR', 'Revenue_INR', 'Profit_INR',
            'Disease_Pest_Risk_pct'
        ]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(r'[^0-9.-]', '', regex=True), errors='coerce')

        print("Data successfully extracted, cleaned, and standardized.")
    else:
        df = pd.DataFrame()
except Exception as e:
    print(f"Extraction error: {e}")
    df = pd.DataFrame()

if not df.empty:
    display(df.head())
    print(df.info())
