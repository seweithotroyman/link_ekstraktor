# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 01:27:46 2019

@author: Seweit Hotroiman
"""

from urllib.request import urlopen, urljoin
import re

def download_halaman(url):
    return urlopen(url).read().decode('utf-8')

def tampilkan_lokasi_gbr(page):
    cocokan_link = re.compile('<img[^>]+src=["\'](.*?)["\']',
                            re.IGNORECASE)
    return cocokan_link.findall(page)

if __name__ == '__main__':
    target_url = input("Masukkan link website :")
    website = download_halaman(target_url)
    lokasi_gbr = tampilkan_lokasi_gbr(website)
    
    for src in lokasi_gbr:
        print(urljoin(target_url, src))
