import json
import os
import random
import webbrowser
from collections import defaultdict


# Path to the Google Chrome Bookmarks file on a MacBook
bookmarks_file = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Bookmarks")

# Load the Bookmarks file
with open(bookmarks_file, "r", encoding="utf-8") as file:
    bookmarks_data = json.load(file)


def extract_urls_by_folder(bookmark_node, parent_name=""):
    """Extracts all URLs from a Chrome bookmark node and organizes them by folder."""
    urls_by_folder = defaultdict(list)
    if 'children' in bookmark_node:
        current_folder = parent_name if parent_name else bookmark_node.get('name', 'root')
        for child in bookmark_node['children']:
            child_urls_by_folder = extract_urls_by_folder(child, current_folder)
            for folder, urls in child_urls_by_folder.items():
                urls_by_folder[folder].extend(urls)
    elif 'url' in bookmark_node:
        urls_by_folder[parent_name].append(bookmark_node['url'])
    return urls_by_folder


# Extract URLs by folder from all roots
all_urls_by_folder = defaultdict(list)
for key in ["bookmark_bar", "other", "synced"]:
    if key in bookmarks_data["roots"]:
        urls_by_folder = extract_urls_by_folder(bookmarks_data["roots"][key])
        for folder, urls in urls_by_folder.items():
            all_urls_by_folder[folder].extend(urls)

# Write URLs by folder to a text file
with open("sorted_urls_by_folder.txt", "w") as output_file:
    for folder, urls in sorted(all_urls_by_folder.items()):
        output_file.write(f"Folder: {folder}\n")
        for url in sorted(urls):
            output_file.write(f"    {url}\n")
        output_file.write("\n")

# Choose a random URL from all URLs and open it in the browser
all_urls = [url for urls in all_urls_by_folder.values() for url in urls]
if all_urls:
    random_url = random.choice(all_urls)
    webbrowser.open(random_url)
    print(f"Opened: {random_url}")
else:
    print("No bookmarks found.")

