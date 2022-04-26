from gettext import find
from bs4 import BeautifulSoup


with open("home.html", "r") as html_file:
    #Lee el contenido html metiéndolo en una variable
    content = html_file.read()

    #Metemos la variable con el html, junto con el parser que utilizaremos
    soup = BeautifulSoup(content, "lxml")

    #Encuentra el primer elemento que especifiquemos, y luego para.
    tags = soup.find("script")

    #Encuentra todos los elementos que especifiquemos.
    tags2 = soup.find_all("script")

    courses_html_tags = soup.find_all("li")

    #Una forma bastante limpia de obtener palabras concretas.
    # for course in courses_html_tags:
    #     print(course.text)

    #Aquí podemos encontrar los precios del tag.

def write(nombre, precio):
    with open ("prueba.txt","w") as f:
        f.write(nombre)
        f.write("\n")
        f.write(precio)
        f.write("\n")

def find_price():
    course_cards = soup.find_all("div",class_="caption")
    for course in course_cards:
        course_name = course.p.text
        course_price = course.h4.text
        write(course_name, course_price)
    print(soup)

find_price()