#!/bin/bash

# Install required packages
pip install -r requirements.txt

# Optional: create directories if not exist
mkdir -p data models notebook

# Optional: Download dataset from Kaggle (if you add API keys)
# kaggle datasets download -d adityakadiwal/water-potability -p data --unzip

echo "✅ Environment setup complete. Ready to run Streamlit app!"