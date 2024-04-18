import requests
import pandas
from bs4 import BeautifulSoup
url="https://ticker.finology.in/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
a=soup.find("table",class_="table table-sm table-hover screenertable")
c=a.find_all("th")
b=[]
for i in c:
    A=i.text
    b.append(A)
df=pandas.DataFrame(columns=b)
d=a.findAll("tr")
for i in d[1:]:
    e=i.find_all("td")
    rows=[j.text.strip() for j in e]
    l=len(df)
    df.loc[l]=rows
df.to_csv("Stock_Market_Data.csv")
print(df)