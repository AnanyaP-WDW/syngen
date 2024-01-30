import requests
import json_repair
import random

class SynGen:
    def __init__(self,
                 anyscale_API_KEY:str,
                 intro_prompt:str,
                 json_prompt:str,
                 #json_repair_prompt:str,
                 #seed:int = 42
                 ):

        self.anyscale_API_BASE = "https://api.endpoints.anyscale.com/v1"
        self.anyscale_API_KEY = anyscale_API_KEY
        self.MODELS = [
    "meta-llama/Llama-2-13b-chat-hf",
    "meta-llama/Llama-2-70b-chat-hf",
    "mistralai/Mistral-7B-Instruct-v0.1",
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "HuggingFaceH4/zephyr-7b-beta",
    "Open-Orca/Mistral-7B-OpenOrca"]
        self.intro_prompt = intro_prompt
        self.json_prompt = json_prompt
        #self.json_repair_prompt = json_repair_prompt
        #random.seed(self.seed)

    def randomize_model(self):
      """ deafault seed set to 42"""

      return random.choice(self.MODELS)

    def get_chat_completion(self, text_1:str):
        model = self.randomize_model()
        url = f"{self.anyscale_API_BASE}/chat/completions"
        body = {
            "model": f"{model}",
            "messages": [{"role": "user", "content": text_1}],
            "temperature": 0.0,
            "max_new_tokens": 5,
            "repetition_penalty": 1.1
        }

        with requests.post(url, headers={"Authorization": f"Bearer {self.anyscale_API_KEY}"}, json=body) as response:
            if response.status_code == 200:
                response_data = response.json()
                ai_message = response_data['choices'][0]['message']['content']
                return ai_message
            else:
                return f"Error: {response.status_code}, {response.text}"



    def generate_synthetic_data(self, review_prompt):


        final_prompt = self.intro_prompt + review_prompt + self.json_prompt
        output = self.get_chat_completion(final_prompt)

        try:
            decoded_object = json_repair.loads(output)
        except Exception:
            print("Failed to manually repair JSON. Shifting to json_repair_with_llm")
            # try:
            #     decoded_object = self.get_chat_completion(self.json_repair_prompt)
            # except Exception:
            #     print("Failed to fix JSON")

        return decoded_object

    def run (self,iter:list):
      results = dict()
      fails = dict()
      for it,review_prompt in enumerate(iter):
        try:
          results[it] = self.generate_synthetic_data(review_prompt)
        except Exception:
          fails[it] = "Failed"

      return results,fails
    