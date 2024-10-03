#!/usr/bin/bash

# create virtual environment 
python3 -m venv .venv 
source .venv/bin/activate

# setup pip and packages
pip install --upgrade pip
pip install -r requirements.txt
