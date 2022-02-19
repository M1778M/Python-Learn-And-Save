import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.google.com/'

client = uReq(url)

page = client.read()


client.close()

pgsoup = soup(page,'html.parser')

print(pgsoup.h2)

print(pgsoup.body.span)

div_class = pgsoup.findAll('div',{"class" : 'search'})
print(div_class)







