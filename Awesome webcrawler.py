__author__ = 'Ajithkumarsekar'
import requests
from bs4 import BeautifulSoup
def google_crawl():
    url=input("Enter the page URL:")
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"html.parser")
    fre=0
    for link in soup.findAll('a'):
        fre+=1
        href=link.get('href')
        print(href)
    print("Total number of links in the page :",fre)

google_crawl()

