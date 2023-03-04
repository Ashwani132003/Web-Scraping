import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=dog&sxsrf=AJOqlzV-NWEyCrksA5NrcKEutCgM79-X4w:1677677253316&source=lnms&tbm=isch&sa=X&ved=2ahUKEwib_Ozl6rr9AhVBTWwGHUtsDP4Q_AUoAXoECAEQAw&biw=1536&bih=796&dpr=1.25#imgrc=eQsdEWaZ6MHrQM'
# url = 'https://en.wiktionary.org/wiki/dog#/media/File:YellowLabradorLooking.jpg'

html = requests.get(url)
content = html.content

parse = BeautifulSoup(content,'html.parser')
# print(parse.prettify)

img = parse.find('img')
print(img)
link = img['src']
with open(f'img.jpg', 'wb') as f:
    response = requests.get(link)
    image = response.content
    f.write(image)