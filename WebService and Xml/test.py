import json
from urllib.request import urlopen
url=urlopen('http://py4e-data.dr-chuck.net/comments_1411163.json').read().decode('utf-8')

url=json.loads(url)
k=0
for i in url['comments']:
    k+=int(i["count"])
print(k)
