#!/bin/bash

if [ ! -f model.gguf ]; then
  echo "Downloading AI model (TinyLlama Q2)..."
  wget https://huggingface.co/tensorblock/tiny-random-llama-GGUF/resolve/main/tiny-random-llama-Q8_0.gguf
fi

uvicorn main:app --host 0.0.0.0 --port 10000
