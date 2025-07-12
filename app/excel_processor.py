import pandas as pd
from typing import List, Dict
from io import BytesIO

# Leer fichero excel y convertirlo en una lista de diccionarios
def process_excel( file: BytesIO ) -> List[Dict]:
    df = pd.read_excel( file )
    return df.to_dict( orient="records" )