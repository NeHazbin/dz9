from tkinter import *
from bs4 import BeautifulSoup
import requests
root = Tk()
sourse = requests.get("https://minfin.com.ua/currency/mb/")
main_text=sourse.text
soup = BeautifulSoup(main_text,features="html.parser")
table = soup.find("table", {"class": "mb-table-currency"})
tr = table.find("td", {"class": "active"})
tr=tr.text
tr = tr[:7]

print(tr)

root.geometry("250x130")
root.title("Конвертер")
currency = Label(root, text="Виберіть валюту")
currency.grid(row=0, column=0, sticky="w")
dollar = Radiobutton(root, text="Доллар")
dollar.grid(row=0, column=1)
currencyVal = IntVar()
currencyVal.set(25)
dollar = Radiobutton(root,  variable=currencyVal, value=36.5686)
rate = Label(root, text="Курс")
rate.grid(row=2, column=0, sticky="w" )
rate_value = Label(root, text="25")
rate_value.grid(row=2, column=1, sticky='w')
def currency_check():
    rate_value.config(text=currencyVal.get())
    dollar = Radiobutton(root,text= "Доллар" ,variable = currencyVal,value = 25,command = currency_check)
suma = Label(root, text= "Введіть суму у валюті" )
suma.grid(row=3, column=0, sticky= "w")
suma_entry = Entry(root)
suma_entry.grid(row=3, column=1, sticky="w")
suma_entry.insert(1, "0")
convert = Button(root, text="Конвертувати")
convert.grid(row=4, column=0, sticky="w")
label = Label(root, text="")
label.grid(row=4, column=1, sticky="w")
def calculate(event):
    label.config(text=currencyVal.get() * int(suma_entry.get()))
    convert.bind( "  <Button - 1>" , calculate)