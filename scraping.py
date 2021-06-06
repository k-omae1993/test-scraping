import argparse
import os
from selenium import webdriver
from bs4 import BeautifulSoup as bs4
import requests
import time
from save_image import save_image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser for Scraping")
    parser.add_argument('--url', type=str, help='path to url')
    parser.add_argument('--name', type=str, help='path to name')
    parser.add_argument('--i', type=int, help='path to i')
    parser.add_argument('--image_path', type=str, help='path to image_path')
    args = parser.parse_args()

    
    
    browser = webdriver.Chrome()
    browser.get('https://google.com')
    time.sleep(2)
    search_bar = browser.find_element_by_name('q')
    search_bar.send_keys('バイクヘルメット 画像')
    search_bar.submit()
    time.sleep(2)
    browser.get('https://www.gettyimages.co.jp/%E5%86%99%E7%9C%9F/%E3%83%90%E3%82%A4%E3%82%AF%E3%83%98%E3%83%AB%E3%83%A1%E3%83%83%E3%83%88')
    time.sleep(2)
    #elements = []
    #for elem_h3 in browser.find_elements_by_xpath('//a/h3'):
        #elem_a = elem_h3.find_element_by_xpath('..')
        #elements.append(elem_a.get_attribute('href'))
    url = args.url
    name = args.name
    image_path = args.image_path
    browser.get(url)
    time.sleep(2) 

    save_image(url=url, name=name, image_path=image_path, i=args.i)
    browser.quit()




