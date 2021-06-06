from bs4 import BeautifulSoup as bs4
import requests
import time

def save_image(url, name, image_path, i):
    url = url
    res = requests.get(url)
    soup = bs4(res.content, 'html.parser')
    img_list = soup.select(name)

    i = i
    for target in img_list:
        re = requests.get(target['src'])
        with open(str('../image_datasets/'+image_path+'/img_'+str(i)+str('.jpeg')), 'wb')as f:
            f.write(re.content)
        i += 1