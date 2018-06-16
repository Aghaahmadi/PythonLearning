import urllib.request

from bs4 import BeautifulSoup

# Fetch URL
url = "http://www.asriran.com/fa/news/614940"
request = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/35.0.1916.47 Safari/537.36 '
    }
)
print(request)
request.add_header('Accept-Encoding', 'utf-8')

# Response has UTF-8 charset header,
# and HTML body which is UTF-8 encoded
response = urllib.request.urlopen(request)
# Parse with BeautifulSoup
soup = BeautifulSoup(response, "html.parser")

# Print title attribute of a <div> which uses umlauts (e.g. können)

print(soup.find('div', id='navbutton_account')['title']).encode('utf-8')
