import requests
import bs4
import csv
from itertools import zip_longest

amazon_products = []
amazon_prices = []

jumia_products = []
jumia_prices = []

print("IN AMAZON.EG WEB-SITE:")
print()

result1 = requests.get("https://www.amazon.eg/s?crid=1LQ9OEFFAFHYO&k=ps5%20console&language=en_AE&ref=glow_cls&refresh=1&sprefix=ps5%2Caps%2C741")

cont1 = result1.content
soup1 = bs4.BeautifulSoup(cont1,"html.parser")


product_title_amazon = soup1.find_all("span",{"class":"a-size-base-plus a-color-base a-text-normal"})
price_amazon = soup1.find_all("span",{"class","a-price-whole"})




for i in range(len(price_amazon)):
    amazon_products.append(product_title_amazon[i].text)
    amazon_prices.append(price_amazon[i].text)

print(amazon_products)
print(amazon_prices)



print("#"*1000)



print("IN JUMIA WEB-SITE:")
print()

result2 = requests.get("https://www.jumia.com.eg/catalog/?q=ps5+console")


cont2 = result2.content
soup2 = bs4.BeautifulSoup(cont2,"html.parser")

product_title_jumia = soup2.find_all("h3",{"class":"name"})
price_jumia = soup2.find_all("div",{"class","prc"})

for i in range(len(product_title_jumia)):
    jumia_products.append(product_title_jumia[i].text)
    jumia_prices.append(price_jumia[i].text)

print(jumia_products)
print(jumia_prices)

# create csv file for amazon products with price
my_list1 = [amazon_products , amazon_prices ]
exported1 = zip_longest(*my_list1)
with open("E:\سنة تالتة\Trainnig\project\Amazon.csv","w") as amazon_sheet:
    wr = csv.writer(amazon_sheet)
    wr.writerow(["Product Name","Product price"])
    wr.writerows(exported1)

# create csv file for jamia products with price
my_list2 = [ jumia_products , jumia_prices]
exported2 = zip_longest(*my_list2)
with open("E:\سنة تالتة\Trainnig\project\Jumia.csv","w") as jumia_sheet:
    wr = csv.writer(jumia_sheet)
    wr.writerow(["Product Name","Product price"])
    wr.writerows(exported2)

#create aggregate csv file for amazon and jumia products with their prices
my_list1 = [amazon_products , amazon_prices ]
my_list2 = [ jumia_products , jumia_prices]
exported = zip_longest(*my_list1,*my_list2)
with open("E:\سنة تالتة\Trainnig\project\ test.csv","w") as final_sheet:
    wr = csv.writer(final_sheet)
    wr.writerow(["Product Name","Product price"])
    wr.writerows(exported)
