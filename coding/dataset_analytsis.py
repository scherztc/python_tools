# !pip install openai
# !pip install matplotlib
# !pip install seaborn

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# OpenAI

client_openai = OpenAI (
		    api_key = os.getenv("OpenAI_token"),
                )

# LM Studio

# client_lmstudio = OpenAI (
#		    base_url = "http://localhost:1234/v1"
#                )


clients = { 
     "gpt-40-mini": client_openai,
#     "meta-llama-3.1-8b-instruct": client_lmstudio
     }


for client_name, client in clients.items():
    print (client_name, client)
