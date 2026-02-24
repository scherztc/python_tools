#Assignment Content
#Question <bdi></bdi>
#Lab Name: Build a Document-Based Chatbot



#Description:

#Create a chatbot using the Llama-Index and various LLM APIs. This lab guides you through integrating document processing capabilities into a chatbot, offering a hands-on experience in advanced conversational AI.



#Recommended Industries:

#Customer Service
#Legal
#Education
#Government Services
#Healthcare


#Prerequisites:

#Intermediate Python, basic understanding of APIs and data processing.



#Access Link:

#https://colab.research.google.com/drive/1H3uP47S0Rvy4apZr_H1YL-_h290XoxZd?usp=sharing

%%capture
#@title Installing required libraries and downloading data.
#@markdown This section will install necessary libraries and setup the environment.

#@markdown Press ▶

# Installation commands
!pip install llama-index
!pip install ipywidgets
!pip install openai
!pip install httpx==0.27.2

# download files
!mkdir data
!gdown --id 15N9bj_2FaHmKphQxYUMn18RZsmWE7mVV -O data/paul_graham_essay.txt

#@title Importing required libraries!

#@markdown Press ▶

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core import PromptTemplate
from llama_index.core import Settings
from IPython.display import Markdown, display
import ipywidgets as widgets
import os

from openai import OpenAI as opai

from PIL import Image

lmscode = "CQvbNUcHYJ9oDLrg"
key = {
    "1": "3",
    "2": "2",
    "3": "4",
    "4": "3",
    "5": "3",
}
user_answers = {}

# Function to check answers and calculate score
def grade(user_answers, key):
    correct_answers_count = 0
    unanswered_questions = []
    final_score = 0
    is_perfect = False  # Initialize the perfection flag as False

    for question, correct_answer in key.items():
        user_answer = user_answers.get(question)
        if user_answer is None:
            unanswered_questions.append(question)  # Collecting unanswered questions
            continue  # Skip further processing for this iteration

        if user_answer == correct_answer:
            print(f"Question {question}: Correct!")
            correct_answers_count += 1
        else:
            #print(f"Question {question}: Incorrect! The answer is {correct_answer}")
            print(f"Question {question}: Incorrect!")

    total_questions = len(key)
    if unanswered_questions:
        print("You have not answered all the questions. Please complete the following questions before getting your final grade:")
        print(", ".join(unanswered_questions))
    else:
        # Calculate and print final score if all questions are answered
        final_score = correct_answers_count / total_questions * 100  # Final score as a percentage
        is_perfect = correct_answers_count == total_questions  # Set perfection flag based on score
        print("--------------------------------------------------------------------------")
        print(f"Final Score: {final_score}% ({correct_answers_count} out of {total_questions} correct)")
        print("--------------------------------------------------------------------------")

    return final_score, is_perfect

#@title Setup OpenAI API Key
#@markdown You need an `OPENAI API` key to be able to run this code.

#@markdown Please `copy + paste` the API code provided to you on Blackboard. **Keep this key private!**

openai_api_key = "" #@param {type:"string"}
import os

os.environ["OPENAI_API_KEY"] = openai_api_key

#@markdown Press ▶

#@title Testing the OpenAI connection
#@markdown Now ask ChatGTP (GPT3.5-turbo) a question to make we have access to the model. Let's also analyze the response!

user_question = "count to 10" #@param {type:"string"}


if user_question != "":
    display(Markdown(f"<i>AI is thinking...</i>"))
    client = opai()
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': user_question}
        ],
        temperature=0,
    )

    # Formatting the response for display
    # Assuming response.choices[0].message.content contains the reply
    # Adjust according to the response structure
    ai_response = response.choices[0].message.content if response.choices else "No response."

    display(Markdown(f"<b>AI RESPONSE:</b> {response}"))
else:
    print(f"No question provided. Please ask a question.")

#@markdown Press ▶

#@title We can filter out the message to something more readable.

#@markdown The rest of the information is very important... but thats for a more advanced lesson.
display(Markdown(f"<b>AI RESPONSE:</b> {response.choices[0].message.content}"))

#@markdown Press ▶

#@title Callout: Managing Tokens (Bonus)

#@markdown Language models read and write text in chunks called tokens. In English, a token can be as short as one character or as long as one word (e.g., a or apple), and in some languages tokens can be even shorter than one character or even longer than one word.

#@markdown For example, the string `"ChatGPT is great!"` is encoded into six tokens: `["Chat", "G", "PT", " is", " great", "!"]`.

#@markdown The total number of tokens in an API call affects:

#@markdown - How much your API call costs, as you pay per token
#@markdown - How long your API call takes, as writing more tokens takes more time
#@markdown - Whether your API call works at all, as total tokens must be below the model’s maximum limit (4097 tokens for gpt-3.5-turbo)
#@markdown - Both input and output tokens count toward these quantities. For example, if your API call used 10 tokens in the message input and you received 20 tokens in the message output, you would be billed for 30 tokens.

#@markdown *Note however that for some models the price per token is different for tokens in the input vs. the output (see the [pricing](https://openai.com/pricing) page for more information).*

#@markdown To see how many tokens are used by an API call, check the usage field in the API response (e.g., response['usage']['total_tokens']).

#@markdown Chat models like gpt-3.5-turbo and gpt-4-turbo-preview use tokens in the same way as the models available in the completions API, but because of their message-based formatting, it's more difficult to count how many tokens will be used by a conversation.

#@markdown Let's check out the total tokens we used above in our request!

#@markdown Press ▶

print(f"Total tokens used: {response.usage.total_tokens}")
