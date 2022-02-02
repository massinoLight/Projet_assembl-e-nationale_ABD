import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://www2.assemblee-nationale.fr/deputes/fiche/OMC_PA267766")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])