#!/bin/bash

if [ ! -f model.gguf ]; then
  echo "Downloading AI model (TinyLlama Q2)..."
  wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q2_K_M.gguf -O model.gguf
fi

uvicorn main:app --host 0.0.0.0 --port 10000
