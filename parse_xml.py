import xml.etree.ElementTree as ET

tree = ET.parse("kaveh.xml")
root = tree.getroot()
for app in root.findall('ReportFooter/Section/Subreport/ReportHeader/Section/Text/TextValue'):
    print(app.text)
    for l in app.findall('TextValue'):
        print(l.text)
