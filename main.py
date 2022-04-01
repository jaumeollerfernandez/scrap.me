from gettext import textdomain
from bs4 import BeautifulSoup
import requests

text_html = requests.get("192.168.1.1:81").text
print(text_html)