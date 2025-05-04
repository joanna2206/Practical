#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

def welcome():
    print("****** Welcome to Food Shop, I am Jelly created by Joanna ******")
    print()

def info():
    global name
    name = input("Can I know your good name: ")
    print("Hey " + name + "! Good to see you here!!!")
    print("You are in the right place. I will help you to book your dish and drinks.")
    print()

def menu():
    print('''Here is your menu with their prices
1. Pizza - ₹200
2. Mango Juice - ₹70
3. Apple Juice - ₹80''')
    print()

def order(price, product):
    print("Thank you for choosing " + product)
    print()
    print("Please give us some more information about you!!!!")
    mob = input("Enter your mobile number: ")
    add = input("Enter your address of delivery: ")
    print('''Choose mode of payment:
1. Online
2. Cash on delivery''')
    pay = input()
    paymode = "Online" if pay == "1" else "Cash on delivery"
    print()
    print("******* Here is the detail of your selected order *******")
    print()
    print("Customer Name : " + name)
    print("Product Name : " + product)
    print("Price : ₹" + str(price))
    print("Payment Mode : " + paymode)
    print("Delivery Addr : " + add)
    print()
    return paymode, add

def choice():
    print("Please select a product you wish to order:")
    a = input().lower()
    price = 0
    product = ""
    if a == "pizza":
        price = 200
        product = "Pizza"
    elif a == "mango juice":
        price = 70
        product = "Mango Juice"
    elif a == "apple juice":
        price = 80
        product = "Apple Juice"
    else:
        print("You have not selected any valid product... Thank you for visiting! Have a nice day!")
        return
    paymode, add = order(price, product)
    print("Please confirm by pressing 1, or 0 to cancel: ")
    b = input()
    print()
    if b == "1":
        print("******* Your order is booked successfully *******")
        print("Customer Name : " + name)
        print("Product Name : " + product)
        print("Price : ₹" + str(price))
        print("Payment Mode : " + paymode)
        print("Delivery Addr : " + add)
        print()
        print("Thank you for your interest !!! Have a nice day !!!")
    else:
        print("***** Thank you for visiting !!! Have a nice day !!!")

def main():
    welcome()
    info()
    menu()
    choice()

if __name__ == "__main__":
    main()


# In[ ]:




