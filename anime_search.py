from sqlite3 import paramstyle
import requests
from bs4 import BeautifulSoup

anime_name = input("Enter the name of the anime you want to search: ")

page = requests.get('https://animixplay.to/?q=' + anime_name)

print(page.content)
    