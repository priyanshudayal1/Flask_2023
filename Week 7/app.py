import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
n=input("Enter what you want to search: ")
l=n.split()
print(l)
s1=l[0]
for i in range(1,len(l)):
    s1="%20"+l[i]
flipkart_url="https://www.flipkart.com/search?q="+str(s1)
f=open("data.txt","w")

clienturl=urlopen(flipkart_url)
flipkart_page=clienturl.read()

flip_html=bs(flipkart_page,"html.parser")
bigbox=flip_html.findAll("div",{"class":"_1AtVbE col-12-12"})

del bigbox[0:3]
 
prod_link="https://www.flipkart.com"+bigbox[3].div.div.div.a['href']

prod_req=requests.get(prod_link)

prod_html=bs(prod_req.text,"html.parser")
comment_box=prod_html.find_all("div",{"class":"_16PBlm"})

try:
    #consumer name
    f.write("The names of the consumers\n")
    for i in comment_box:
        obj=i.div.div.find_all('p',{"class":"_2sc7ZR _2V5EHH"})[0].text
        f.write(obj+"\n") 
except Exception as e:
    print("consumer name written")
    f.write("\n \n")

try:
    #rating
    f.write("The ratings\n")
    for i in comment_box:
        obj=i.div.div.div.div.text
        f.write(obj+"\n")      
except Exception as e:
    print("rating written")
    f.write("\n \n")

try:
    #comment head
    f.write("The comments head\n")
    for i in comment_box:      
        obj=i.div.div.div.p.text
        f.write(obj+"\n") 
except Exception as e :
    print("comments head written")     
    f.write("\n \n")

try:
    #full comment
    f.write("The full comments\n")
    for i in comment_box:
        obj=i.div.div.find_all('div',{"class":""})[0].div.text
        f.write(obj+"\n")     
except Exception as e:
    print("full comment written")
    f.write("\n \n")




# print("_________________________---------------------------------------------------")
# for i in bigbox:
#     print(j)
#     url1="https://www.flipkart.com"+i.div.div.div.a['href']
#     print(url1)