# Tokener Pro — OpenAI-Compatible Minimax API

**Fast, cheap, and reliable API proxy powered by Minimax.**

## Why Tokener Pro?

| Feature | OpenAI | Tokener Pro |
|---------|--------|-------------|
| Price | 0.002/1Ktokens∣∗∗0.0004/1K tokens** |
| Latency | ~1-3s | **<500ms** |
| API Format | OpenAI compatible | ✅ 100% compatible |

Replace your OpenAI base URL with `https://renrenfa.top/v1` — zero code changes needed.

## Quick Start

### Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_TOKENER_API_KEY",  # Get from https://renrenfa.top
    base_url="https://renrenfa.top/v1"
)

response = client.chat.completions.create(
    model="minimax-01",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)


      



Node.js




      

import OpenAI from 'openai';

const client = new OpenAI({
    apiKey: 'YOUR_TOKENER_API_KEY',
    baseURL: 'https://renrenfa.top/v1'
});

const response = await client.chat.completions.create({
    model: 'minimax-01',
    messages: [{role: 'user', content: 'Hello!'}]
});
console.log(response.choices[0].message.content);


      



cURL




      

curl https://renrenfa.top/v1/chat/completions \ 
  -H "Content-Type: application/json" \ 
  -H "Authorization: Bearer YOUR_TOKENER_API_KEY" \ 
  -d '{"model": "minimax-01", "messages": [{"role": "user", "content": "Hello!"}]}'


      



Supported Models



minimax-01 — Latest high-performance model

minimax-t2i — Text-to-image model



Get Started



Sign up at https://renrenfa.top

Get your API key from dashboard

Replace api_key and base_url as shown above



Pricing




        

PlanPriceTokens/monthFree$01MStarter$950MPro$29200MEnterpriseCustomUnlimited

Full pricing: https://renrenfa.top



Support



Documentation: https://renrenfa.top

Email: support@renrenfa.top



License

MIT
