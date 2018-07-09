import pandas as pd
url = "http://codal.ir/Reports/Decision.aspx?LetterSerial=lOCU3hBfbCpdGw8UrgfDbw%3d%3d&rt=0&let=58&ct=0"
table = pd.read_html(url, encoding='UTF-8')

hd = table[1].values[1]
headers = []
for h in hd:
    headers.append(h)

