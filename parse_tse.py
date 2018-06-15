import requests
from bs4 import BeautifulSoup

# Collect and parse first page
page = requests.get('http://www.tsetmc.com/Loader.aspx?ParTree=151312')
# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='t0c5 ch0')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

print(type(artist_name_list_items))

for result in artist_name_list_items:
    print(result)