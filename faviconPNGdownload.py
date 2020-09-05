#! /usr/bin/python3
import urllib.request
url = input("Enter URL> ")
size=input("Size (e.g.) 32, 64, 128> ")
file= f"{url.split('/')[-1]}{size}x{size}.png"
urllib.request.urlretrieve(f"http://www.google.com/s2/favicons?sz={size}&domain_url={url}", file)
