from flask import Flask,request,render_template
from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen as uReq
import logging
import os
j=0
save_directory="images/"
search=input("Enter product: ")
search.replace(" ","")
url="https://www.meesho.com/search?q=shirt&searchType=manual&searchIdentifier=text_search"
search=uReq(f"https://www.flipkart.com/search?q={search}+&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_6_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_6_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=iphone15+&requestId=bfa3be85-655b-4004-a2eb-423a5d022cc8&as-backfill=on")
src=search.read()
soup=bs(src,"html.parser")
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
imgs=soup.find_all("img",{"class":"_396cs4"})
for i in imgs:
    
    img_url=i['src']
    img_data=requests.get(img_url).content
    with open(os.path.join(save_directory, "photo"+str(j)+".jpg"), "wb") as f:
        f.write(img_data)
    j=j+1