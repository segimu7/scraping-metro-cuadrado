import requests
from bs4 import BeautifulSoup

r = requests.get(r"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xiphone.TRS0&_nkw=iphone&_sacat=0")
c = r.content
soup = BeautifulSoup(c,"html.parser")

all = soup.findAll("li",{"class":"s-item"})    

print(all[0])