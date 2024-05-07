import json
import os
import random
import webbrowser

# Path to the Google Chrome Bookmarks file on a MacBook
bookmarks_file = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Bookmarks")

# Load the Bookmarks file
with open(bookmarks_file, "r", encoding="utf-8") as file:
    bookmarks_data = json.load(file)

def extract_urls(bookmark_node):
    """Extracts all URLs from a Chrome bookmark node."""
    urls = []
    if 'children' in bookmark_node:
        for child in bookmark_node['children']:
            urls.extend(extract_urls(child))
    elif 'url' in bookmark_node:
        urls.append(bookmark_node['url'])
    return urls

# Extract all URLs from all roots
urls = []
for key in ["bookmark_bar", "other", "synced"]:
    if key in bookmarks_data["roots"]:
        urls.extend(extract_urls(bookmarks_data["roots"][key]))

# Sort URLs alphabetically
urls = sorted(urls)

# Write URLs to a text file
with open("sorted_urls.txt", "w") as output_file:
    for url in urls:
        output_file.write(url + "\n")

# Choose a random URL and open it in the browser
if urls:
    random_url = random.choice(urls)
    webbrowser.open(random_url)
    print(f"Opened: {random_url}")
else:
    print("No bookmarks found.")

