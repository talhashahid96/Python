import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime
import time
from tkinter import *


def gui(window, frame):
    frame.pack(pady=20)
    label_productname = Label(frame, text="Product Name")
    label_productname.grid(row=0, column=0, padx=10, pady=5)
    label_price = Label(frame, text="Price")
    label_price.grid(row=0, column=1, padx=20, pady=10)
    label_date = Label(frame, text="Date")
    label_date.grid(row=0, column=2, padx=30, pady=15)
    label_time = Label(frame, text="Time")
    label_time.grid(row=0, column=3, padx=40, pady=20)


window = Tk()
frame = Frame(window)
window.geometry("700x500")
gui(window, frame)
window.title("Price getter")
url = "https://saudi.jazp.com/sa-en/iSonic-IH909-3-in-1-Grooming-Set--/p/94067"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")
item = soup.find(class_="titlepro col-sm-10 nopadlr")
if item:
    item_name = item.text.strip()
    print("Item Name :", item_name)
else:
    print("Item not found.")
price = soup.find(class_="price-details d-flex align-item-center")
if price:
    item_price = price.text.strip()
    print("Item Price Details :", item_price)
else:
    print("Price not found.")
headers = ["Product", "Price", "Date", "c_time"]
date = datetime.date.today()
print(date)
c_time = time.strftime("%H:%M:%S")
print(c_time)
data = [item_name, item_price, date, c_time]
with open("Price Check.csv", "w", newline="", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerow(data)


def get_price():
    url = "https://saudi.jazp.com/sa-en/iSonic-IH909-3-in-1-Grooming-Set--/p/94067"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    item = soup.find(class_="titlepro col-sm-10 nopadlr")
    if item:
        item_name = item.text.strip()
        print("Item Name :", item_name)
    else:
        print("Item not found.")
    price = soup.find(class_="price-details d-flex align-item-center")
    if price:
        item_price = price.text.strip()
        print("Item Price :", item_price)
    else:
        print("Price not found.")
    headers = ["Product", "Price", "Date", "c_time"]
    date = datetime.date.today()
    print(date)
    c_time = time.strftime("%H:%M:%S")
    print(c_time)
    data = [item_name, item_price, date, c_time]
    with open("Price Check.csv", "a", newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(data)
    label_productname = Label(frame, text=item_name)
    label_productname.grid(row=1, column=0, padx=10, pady=5)
    label_price = Label(frame, text=item_price)
    label_price.grid(row=1, column=1, padx=20, pady=10)
    label_date = Label(frame, text=date)
    label_date.grid(row=1, column=2, padx=30, pady=15)
    label_time = Label(frame, text=c_time)
    label_time.grid(row=1, column=3, padx=40, pady=20)


button = Button(window, text="Get Price", command=get_price, bg="Beige", font=("Calibri", 12), activeforeground="White",
                activebackground="Green")
button.pack(pady=15)
window.mainloop()
# while True:
# get_price()
# time.sleep(5)
