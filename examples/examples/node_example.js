/**
 * Tokener Pro — Node.js Example
 * OpenAI-compatible Minimax API
 */

import OpenAI from 'openai';

const client = new OpenAI({
    apiKey: process.env.TOKENER_API_KEY || 'YOUR_TOKENER_API_KEY',
    baseURL: 'https://renrenfa.top/v1'
});

// Text completion
async function chat() {
    const response = await client.chat.completions.create({
        model: 'minimax-01',
        messages: [
            {role: 'system', content: 'You are a helpful assistant.'},
            {role: 'user', content: 'What is the capital of France?'}
        ],
        temperature: 0.7
    });
    console.log('Chat:', response.choices[0].message.content);
}

// Image generation
async function image() {
    const response = await client.images.generate({
        model: 'minimax-t2i',
        prompt: 'A beautiful sunset over Paris',
        size: '1024x1024'
    });
    console.log('Image URL:', response.data[0].url);
}

chat().then(() => image());
