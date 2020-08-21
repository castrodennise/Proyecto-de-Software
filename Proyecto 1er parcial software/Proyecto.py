from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import requests

stack = 'https://es.stackoverflow.com/users/'
user = input('inserte ID:')
stack = stack + str(user)+"?tab=tags"
link = requests.get(stack)
html= BeautifulSoup(link.content,'html.parser')
users= html.find_all('a',class_='post-tag')

etiquetas = list()
for i in users:
    etiquetas.append(i.text)
print(etiquetas)

with open("proyecto.txt","w")as file:
    file.write(str(etiquetas))

stopwords = []

doc = open("proyecto.txt","r+")
datos = doc.read().replace("","")

nube = WordCloud(width=500,height=500,background_color='white',stopwords=stopwords,min_font_size=5,max_font_size=500).generate(datos)
nube.to_file('proyecto.png')
print("END")
exit()