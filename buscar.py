from bs4 import BeautifulSoup
import requests

def buscaweb(self, web):
    self.web = web
    self.file = requests.get(web).text
    self.webparsed = BeautifulSoup(self.file, "lxml")

def tipo():
    
