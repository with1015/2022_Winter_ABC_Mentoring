from bs4 import BeautifulSoup
import requests
import argparse

url = "https://www.skysports.com/football/news/11095/12526541/adama-traore-barcelona-in-talks-with-wolves-forward-who-is-unconvinced-by-tottenham-role"
print("Target url:", url)

# Call HTML from url
contents = []
news = requests.get(url)
news_html = BeautifulSoup(news.text,"html.parser")

# Get all "p" tag contents from HTML
contents.append(news_html.find_all('p'))

print(contents)
