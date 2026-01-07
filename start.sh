#!/bin/bash

if [ ! -f model.gguf ]; then
  echo "Downloading AI model (TinyLlama Q2)..."
  wget https://drive.google.com/file/d/1qi4dQG77fqZUz_SXNnX7GQ2JX80vEJ0D/view?usp=sharing
fi

uvicorn main:app --host 0.0.0.0 --port 10000
