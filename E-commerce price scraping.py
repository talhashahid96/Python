import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import datetime

url = "https://www.elo.shopping/products/polo-republica-mens-quilted-puffer-hooded-jacket"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")
title = soup.find('div', class_="product__title")
if title:
    title_name = title.text.strip()
    print("Product Name :", title_name[0:39])
else:
    print("Product not found.")
price = soup.find('span', class_="price-item price-item--sale price-item--last")
if price:
    price_name = price.text.strip()
    print("Price :", price_name)
else:
    print("Price not found.")
day_today = time.strftime("%A")
print("Day :", day_today)
date_today = datetime.date.today()
print("Date :", date_today)
time_now = time.strftime("%I:%M:%S")
print("Time :", time_now)
headers = ["Product Name", "Price", "Date", "Day", "Time"]
data = [title_name, price_name, date_today, day_today, time_now]
with open("Product Price.csv", "w", newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerow(data)


def get_product_price():
    url = "https://www.elo.shopping/products/polo-republica-mens-quilted-puffer-hooded-jacket"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    title = soup.find('div', class_="product__title")
    if title:
        title_name = title.text.strip()
        print("Product Name :", title_name[0:39])
    else:
        print("Product not found.")
    price = soup.find('span', class_="price-item price-item--sale price-item--last")
    if price:
        price_name = price.text.strip()
        print("Price :", price_name)
    else:
        print("Price not found.")
    day_today = time.strftime("%A")
    print("Day :", day_today)
    date_today = datetime.date.today()
    print("Date :", date_today)
    time_now = time.strftime("%I:%M:%S")
    print("Time :", time_now)
    headers = ["Product Name", "Price", "Date", "Day", "Time"]
    data = [title_name, price_name, date_today, day_today, time_now]
    with open("Product Price.csv", "a", newline="", encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)


while True:
    get_product_price()
    time.sleep(86400)
