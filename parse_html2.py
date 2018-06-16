from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.tsetmc.com/loader.aspx?ParTree=151311&i=35425587644337450')
soup = BeautifulSoup(page.text, "html5lib")

print(soup.get_text())