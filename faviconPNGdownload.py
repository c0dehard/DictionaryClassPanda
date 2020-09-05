#! /usr/bin/python3
import urllib.request
url = input("Enter URL> ")
img_size=input("Size (e.g.) 32, 64, 128> ")
filename = url.split('/')[-1]
urllib.request.urlretrieve(f"http://www.google.com/s2/favicons?sz={img_size}&domain_url={url}", filename+".png")
