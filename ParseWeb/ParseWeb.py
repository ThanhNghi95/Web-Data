from urllib.request import urlopen
from bs4 import BeautifulSoup
url='http://py4e-data.dr-chuck.net/known_by_Kasper.html'
for i in range(6):
    html=urlopen(url)
    bsObj= BeautifulSoup(html,'lxml')
    links=bsObj.findAll('a')
    count=0
    for link in links:
        count+=1
        if count>18:
            break
        url=link['href']
html=urlopen(url)
bsObj= BeautifulSoup(html,'lxml')
count=0
name=list()
links=bsObj.findAll('a')
for link in links:
    k=link.text
    name.append(k)
print(name[17])
        






   

 
