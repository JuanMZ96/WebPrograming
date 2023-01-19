from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://argentina.as.com/resultados/futbol/primera/clasificacion/'

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

eq