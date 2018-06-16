import xml.etree.ElementTree as ET
from pyquery import PyQuery
html = 'http://www.tsetmc.com/loader.aspx?ParTree=151311&i=35425587644337450'
tree = PyQuery(html)
root = tree.getroot()
for app in root.findall('ReportFooter/Section/Subreport/ReportHeader/Section/Text/TextValue'):
    print(app.text)
    for l in app.findall('TextValue'):
        print(l.text)
