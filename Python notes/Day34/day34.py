import requests
from bs4 import BeautifulSoup
url = "https://codegnan.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print("Website Title:")
print(soup.title.text)
print("\nHeadings:")
for heading in soup.find_all("h2"):
    print(heading.text.strip())