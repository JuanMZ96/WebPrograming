from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

eq =  soup.find_all('span', class_= 'nombre-equipo')

#print(eq)
for val in eq:
    print(val)