import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=pet+dog&sxsrf=AJOqlzXsj8W5ThdduaqH3d4fYia4MkBe2A:1677900492082&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjY6rG2qsH9AhVu8DgGHcUrDnQQ_AUoAnoECAEQBA&biw=1536&bih=796&dpr=1.25'

html = requests.get(url)
content = html.text

parse = BeautifulSoup(content,'html.parser')

img = parse.find_all('img')

def download_images(images):
    count = 0
    print(f"Total {len(images)} Image Found!")

    if len(images) != 0:
        for i, image in enumerate(images):

            try:
                image_link = image["data-srcset"]                
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:                        
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass
            try:
                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open(f"images{i+1}.jpg", "wb+") as f:
                        f.write(r)
                    count += 1
            except:
                pass    
            
download_images(img)            