import pandas as pd
from typing import List, Dict
from io import BytesIO
import re

# ---------- LIMPIEZA DE COLUMNAS ----------
def clean_column_name(name: str) -> str:
    return re.sub(r'\W+', '_', name.strip().lower())

# ---------- PROCESAMIENTO DE EXCEL ----------
def process_excel(file: BytesIO) -> List[Dict[str, any]]:
    df = pd.read_excel(file)
    df.columns = [clean_column_name(col) for col in df.columns]
    df = df.where(pd.notnull(df), None)
    return df.to_dict(orient="records")
    
