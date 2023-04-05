import requests
import pandas as pd
from bs4 import BeautifulSoup

product_name = []
price = []
Description = []
for i in range(1,25):
    url ='https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)

    r = requests.get(url)
    #print(r)
    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")
    for i in names:
        name = i.text
        product_name.append(name)

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for j in prices:
        amount = j.text
        price.append(amount)

    desc = box.find_all("ul", class_="_1xgFaf")
    for j in desc:
        d = j.text
        Description.append(d)

df = pd.DataFrame({"Product Name":product_name,"Price":price,"Description":Description})
print(df)

df.to_csv("flipkart_mobiles_under_50000.csv")