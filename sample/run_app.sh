#!/bin/bash
#nohup uvicorn app:app --host 0.0.0.0 --port 8000 --reload >> run_app.log &
uvicorn app:app --host 0.0.0.0 --port 8000 --reload