# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 00:24:14 2019

@author: hehehe
"""

from urllib.request import urlopen, urljoin
import re

def download_halaman(url):
    return urlopen(url).read().decode('utf-8')

def hasilkan_link(page):
    cocokan_link = re.compile('<a[^>]+href=["\'](.*?)["\']',
                            re.IGNORECASE)
    return cocokan_link.findall(page)

if __name__ == '__main__':
    target_url = input("Masukkan link website :")
    website = download_halaman(target_url)
    links = hasilkan_link(website)
    
    for link in links:
        print(urljoin(target_url, link))
