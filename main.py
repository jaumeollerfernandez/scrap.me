from gettext import textdomain
from bs4 import BeautifulSoup
import requests

text_html = requests.get("http://localhost:81/index_.php").text

file = BeautifulSoup(text_html,"lxml")

with open("prueba.txt", "w") as f:
    f.write("hola")
print(type(file))
