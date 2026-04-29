#!/bin/bash
# Tokener Pro — cURL Example
# OpenAI-compatible Minimax API

# Set your API key
API_KEY="YOUR_TOKENER_API_KEY"
BASE_URL="https://renrenfa.top/v1"

# Chat completion
echo "=== Chat Example ==="
curl $BASE_URL/chat/completions \ 
  -H "Content-Type: application/json" \ 
  -H "Authorization: Bearer $API_KEY" \ 
  -d '{
    "model": "minimax-01",
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
  }'

echo ""
echo "=== Image Example ==="
# Image generation
curl $BASE_URL/images/generations \ 
  -H "Content-Type: application/json" \ 
  -H "Authorization: Bearer $API_KEY" \ 
  -d '{
    "model": "minimax-t2i",
    "prompt": "A beautiful sunset over Paris",
    "size": "1024x1024"
  }'
