#@title Viewing our text data

#@markdown Before we proceed, lets take a quick look at the data we will be querying found in the `data` folder in our files found on the left side.

#@markdown Press ▶

#read and display first 10 sentences of paul_graham_essay.txt
print("From paul_graham_essay.txt:")
print("----------------------------")

with open("data/paul_graham_essay.txt", "r") as f:
    print(f"{f.read()[:980]} .... and so on.")


#@title Let's load the data and build out an embedding Index

#@markdown Press ▶
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
