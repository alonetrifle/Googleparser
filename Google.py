import requests
import time
import re
from bs4 import BeautifulSoup
class Google:
    fname= open("links.txt" , "a+" , encoding = "utf8")
    def __init__(self,parameter):
        self.params= parameter
    def results(self,page = 0):
        self.pages= page
        self.url = f'https://www.google.com/search?nfpr=1&q={self.params}&start={self.pages}'
        self.headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML\
        , like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        rq = requests.get(self.url, headers = self.headers)
        soup = BeautifulSoup(rq.content , "html5lib")
        box = soup.find(id = "search")
        links = box.find_all('div' , class_ = 'r')
        for i in links :
            res = i.find(attrs = {'href':re.compile('http')})
            print(res['href'] ,file = Google.fname)

rng= input('How many pages would you like to parse?\n')
if isinstance(rng, int):
    pass
else:
    print("Please enter an integer!\n")
    exit()
param = input("Enter search phrase:\n")
param.replace(' ' , '+')
pg = 0
google = Google(param )
if int(rng):
    for i in range(rng):
        pg = i*10
        google.results(pg)
