from flask import Flask,request,render_template
from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen as uReq
import logging

# logging.basicConfig(filename="logs.txt",level=logging.NOTSET)

# app=Flask(__name__)

# @app.route("/",methods=["POST","GET"])
# def home():
#     return render_template("index.html")
    
# f=open("test.txt","w")


# @app.route("/search",methods=["GET","POST"])
# def search():
#     if request.method=="GET":
#         return render_template("comments.html")
#     if request.method=="POST":
#         url=request.form.get("link")
#         url_client=uReq(url)
#         yt_page=url_client.read()
#         yt_html=bs(yt_page,"html.parser")
#         comment_box=yt_html.find_all("div",{"class":"style-scope ytd-item-section-renderer style-scope ytd-item-section-renderer"}).content
#         return render_template("comments.html",comments=comment_box)
#     else:
#         return render_template("index.html")

# url=request.form.get("https://www.youtube.com/watch?v=0HWnjM14csE")
url_client=uReq("https://www.youtube.com/watch?v=0HWnjM14csE")
yt_page=url_client.read()
yt_html=bs(yt_page,"html.parser")
# print(yt_html)
comment_box=yt_html.find_all("div",{"class":"style-scope ytd-watch-flexy"})
print(comment_box)

    
# if __name__=="__main__":
#     app.run()

# f.close()