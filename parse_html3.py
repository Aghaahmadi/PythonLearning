import nltk
import urllib.request

url = "http://www.tsetmc.com/loader.aspx?ParTree=151311&i=35425587644337450"
html = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/35.0.1916.47 Safari/537.36 '
    }
)
print(html)
raw = nltk.clean_html(html)
print(raw)