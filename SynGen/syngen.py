import requests
import json_repair
import random
from syngen.config import ANYSCALE_MODELS 


class GenRequest:
    def __init__(self,seed_data=None):
        self.seed_data = seed_data if seed_data is not None else []

class SynGen:
    def __init__(self, anyscale_API_KEY: str, intro_prompt: str, json_prompt: str):

        self.anyscale_API_BASE = "https://api.endpoints.anyscale.com/v1"
        self.anyscale_API_KEY = anyscale_API_KEY
        self.MODELS = ANYSCALE_MODELS
        self.intro_prompt = intro_prompt
        self.json_prompt = json_prompt

    def _randomize_model(self):
        """deafault seed set to 42"""

        return random.choice(self.MODELS)

    def _get_chat_completion(self, text_1: str):
        model = self._randomize_model()
        url = f"{self.anyscale_API_BASE}/chat/completions"
        body = {
            "model": f"{model}",
            "messages": [{"role": "user", "content": text_1}],
            "temperature": 0.0,
            "max_new_tokens": 5,
            "repetition_penalty": 1.1,
        }

        with requests.post(
            url, headers={"Authorization": f"Bearer {self.anyscale_API_KEY}"}, json=body
        ) as response:
            if response.status_code == 200:
                response_data = response.json()
                ai_message = response_data["choices"][0]["message"]["content"]
                return ai_message
            else:
                return f"Error: {response.status_code}, {response.text}"

    def _generate_synthetic_data(self, review_prompt):

        final_prompt = self.intro_prompt + review_prompt + self.json_prompt
        output = self._get_chat_completion(final_prompt)

        try:
            decoded_object = json_repair.loads(output)
        except Exception:
            print("Failed to manually repair JSON")
            decoded_object = None

        return decoded_object

    def run(self, request:GenRequest):
        iter = request.seed_data
        results = dict()
        fails = dict()
        for it, review_prompt in enumerate(iter):
            try:
                results[it] = self._generate_synthetic_data(review_prompt)
            except Exception:
                fails[it] = "Failed"

        return results, fails
