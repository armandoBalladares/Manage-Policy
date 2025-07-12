
# check package

pip list
pip freeze

# Installation

pip install -r requirements.txt

# Run App

uvicorn app.main:app --reload

# Test Implementation
 
curl -X POST "http://127.0.0.1:8000/upload-excel/" \
  -F "file=@/ruta/a/tu/archivo.xlsx"
