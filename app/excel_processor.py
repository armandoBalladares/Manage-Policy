import pandas as pd
from typing import List, Dict
from io import BytesIO

# Leer fichero excel y convertirlo en una lista de diccionarios
def process_excel( file: BytesIO ) -> List[Dict]:
    df = pd.read_excel( file )
    # Reemplazar NaN por None (compatible con JSON/Firebase)
    df =  df.where( pd.notnull(df), None )    
    # Construye una lista de diccionarios con cada fila
    datos_json = [row.dropna().to_dict() for _, row in df.iterrows()]
    return datos_json