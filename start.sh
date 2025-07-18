#!/usr/bin/env bash
# uvicorn app.main:app --host=0.0.0.0 --port=os.environ['PORT']
uvicorn app.main:app --host=0.0.0.0 --port=$PORT
