from bs4 import BeautifulSoup
import requests


def find_and_replace(html_content, keyword, replacement):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all elements containing the keyword
    elements_with_keyword = soup.find_all("span", attrs={"class": "text"})

    # Replace the content of each found element with replacement word
    for element in elements_with_keyword:
        newline = " ".join([replacement if x.lower() in keyword else x for x in element.string.split()])
        element.string = newline

    return str(soup)

# Read the HTML file
file_path = "quotesoverrides/quotes.toscrape.com/index.html"

with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Specify the keyword you want to find and the replacement text
keywords = ["world", "the"]
replacement_text = "REDACTED"

# Find and replace the keyword in the HTML content
modified_html_content = find_and_replace(html_content, keywords, replacement_text)

# Write the modified content back to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(modified_html_content)

print(f'Keyword "{keywords}" replaced with "{replacement_text}" in the file "{file_path}".')
