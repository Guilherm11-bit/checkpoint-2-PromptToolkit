import requests
import os
import time
import tiktoken


class LLMClient:

    def __init__(self):
        self.host = os.getenv("OLLAMA_HOST")
        self.model = os.getenv("MODEL")

    def contar_tokens(self, texto):
        encoder = tiktoken.get_encoding("cl100k_base")
        return len(encoder.encode(texto))

    def chat(self, prompt, system="", temp=0.5, max_tokens=300):

        inicio = time.time()
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False,
            "options": {
                "temperature": temp,
                "num_predict": max_tokens
            }
        }

        response = requests.post(
            f"{self.host}/api/chat",
            json=payload,
            timeout=120
        )

        data = response.json()

        resposta = data["message"]["content"]

        fim = time.time()

        return {
            "resposta": resposta,
            "tokens_prompt": self.contar_tokens(prompt),
            "tokens_resposta": self.contar_tokens(resposta),
            "tempo_ms": round((fim - inicio) * 1000, 2)
        }