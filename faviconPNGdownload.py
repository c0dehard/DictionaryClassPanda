#! /usr/bin/python3
import urllib.request
url = input("Enter URL> ")
filename = url.split('/')[-1]
urllib.request.urlretrieve(f"http://www.google.com/s2/favicons?sz=64&domain_url={url}", filename+".png")
