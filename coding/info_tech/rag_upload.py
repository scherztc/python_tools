#@title Upload your own `.txt` file:

#@markdown Note: This example only works with `.txt`

#@markdown Press ▶

#create new folder named user_data_folder and only do so if one does not exist
import os
if not os.path.exists("user_data_folder"):
    os.mkdir("user_data_folder")


from google.colab import files
uploaded = files.upload() # This will prompt user to upload a csv

for data_file in uploaded.keys():
    # check if the user uploaded a file that does not end in either txt or pdf
    if not data_file.endswith(".txt"):
        print(f"File {data_file} is not a txt. Please re-upload a new file.")
        # delete file that was uploaded
        try:
            os.remove(data_file)
        except:
            pass
        continue

    print(f'User uploaded file "{data_file}"')
    # move the file to user data folder
    os.rename(data_file, f"user_data_folder/{data_file}")


#@title Let's load the data and build out an embedding Index

#@markdown Press ▶
documents = SimpleDirectoryReader("user_data_folder").load_data()
index = VectorStoreIndex.from_documents(documents)

#@title Query, Customize and talk to the LLM on that data!

#@markdown > 💡 `Model Choice`: Keep in mind, gpt-4 costs more per token!
model_choice = 'gpt-3.5-turbo' #@param ["gpt-3.5-turbo", "gpt-4"]

#@markdown \
#@markdown > 💡 `Temperature`: changes how imaginative the model can be.
temperature_choice = "0.1" #@param ["0.1", "0.5", "1.0"]
temperature_choice = float(temperature_choice)

#@markdown \
#@markdown > 💡 `Initial Prompt`: Change how the model acts when formulating its response. For example, you can instruct the model to respond in Spanish, summarize a concept, or generate ideas in a creative manner. Crafting a thoughtful initial prompt is a key part of prompt engineering. Consider specifying the style, tone, or specific details you want the model to include in its response. This helps in obtaining more targeted and useful outputs from the model.
initial_prompt = "" #@param {type:"string"}

#@markdown \
#@markdown > 💡 `Prompt`: Ask the model a question!
#@markdown >> Prompt engineering is a crucial technique in natural language processing, especially with large models like GPT-3. It involves designing prompts that guide the model to generate the desired outputs efficiently. Here are some tips:
#@markdown >> - **Precision in Prompting**: Specificity in prompts leads to more accurate responses.
#@markdown >> - **Iterative Refinement**: Refine prompts based on prior outputs to improve results.
#@markdown >> - **Understanding Capabilities**: Knowing what the model does best can help tailor your prompts.
#@markdown >> - **Use of Instructions**: Direct the model's responses by explicitly stating how it should respond (e.g., list, describe, explain).

question = "" #@param {type:"string"}

#@markdown Press ▶

if question != "":

  # Configuration for the LLM
  Settings.llm = OpenAI(temperature=temperature_choice, model=model_choice)
  query_engine = index.as_query_engine()

  # Prepare prompt
  prompt_string = initial_prompt + ". " + question if initial_prompt else question

  display(Markdown(f"<i>AI is thinking...</i>"))
  # Query and display response
  response = query_engine.query(prompt_string)
  display(Markdown(f"<b>AI RESPONSE:</b> {response}"))

else:
  print("Please provide a question and rerun the cell.")
