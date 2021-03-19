#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlsplit
from tqdm import tqdm

def get_links(url):
    
    # make a http request to get the html page
    page = requests.get(url)
    
    # parse the html
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # find all of the html anchor tags
    tags = soup.find_all('a')
    
    # find the destination of all anchor tags
    hrefs = [tag.get('href') for tag in tags]

    # return a list absolute urls
    urls = [urljoin(url, href) for href in hrefs]
    
    # strip out the first five links of the form:
    # ./?C=N;O=D
    # ./?C=M;O=A
    # ./?C=S;O=A
    # ./?C=D;O=A
    # ./
    urls = urls[5:]
    
    return urls
    

root = 'http://data.pgc.umn.edu/elev/dem/setsm/ArcticDEM/mosaic/v3.0/2m/'


urls = get_links(root)

with open('urls.txt', 'w') as f:
    for url in tqdm(urls):
        links = get_links(url)
        for link in links:
            f.write(link + '\n')

