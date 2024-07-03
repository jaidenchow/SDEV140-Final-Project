import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
#imports for GUI and images

#
#Author: Jaiden Chow
#Date written: 7/3/2024
#Assignment:  Module 06 Project Status Report II 
#Short Desc:  GUI for a boba shop called "BobaBuy", has lots of 
#             functionalities, such as images that show the tea selection and price, 
#             options to select tea, topping, sugar level, and ice level, allows user to add to order and order as much drinks
#             needed, and checkouts the sum of the price of the drinks.
#

# Defines the variables (Different teas, toppings, sugar and ice levels for each button)
tea_types = ["Thai Tea", "Original Milk Tea", "Jasmine Tea", "Strawberry Milk Tea", "Taro Milk Tea", "Brown Sugar Milk Tea"]
toppings = ["Boba", "Jelly", "Lychee"]
sugar_levels = ["100%", "75%", "50%", "25%", "0%"]
ice_levels = ["100%", "50%", "0%"]

tea_prices = {"Thai Tea": "Thai Tea - $5.80",       #correlates each tea to its price
    "Original Milk Tea": "Original Milk Tea - $6.00",
    "Jasmine Tea": "Jasmine Tea - $5.80",
    "Strawberry Milk Tea": "Strawberry Milk Tea - $6.10",
    "Taro Milk Tea": "Taro Milk Tea - $6.30",
    "Brown Sugar Milk Tea": "Brown Sugar Milk Tea - $6.50"}
tea_images = {"Thai Tea": "Thaitea.jpg",
    "Original Milk Tea": "OriginalMilkTea.jpg",
    "Jasmine Tea": "JasmineTea.jpg",                #correlates each tea to the image 
    "Strawberry Milk Tea": "strawberrymilktea.jpg",
    "Taro Milk Tea": "taromilktea.jpg",
    "Brown Sugar Milk Tea": "Brownsugarboba.jpg"}
#Title section, with BobaBuy
window = tk.Tk()
window.title("Welcome to BobaBuy!")
tea_type = tk.StringVar()
topping = tk.StringVar()
sugar_level = tk.StringVar()
ice_level = tk.StringVar()
#Order button, and resets the buttons from previous drinks/orders
orders = []
def add_to_order():
    order = f"You have ordered a {tea_type.get()} with {topping.get()}, {sugar_level.get()} sugar, and {ice_level.get()} ice. Price: {tea_prices[tea_type.get()]}"
    orders.append(order)
    messagebox.showinfo("Order Added", order)
    tea_type.set("")
    topping.set("")
    sugar_level.set("")
    ice_level.set("")
#The checkout button, that sums up the total amount of drinks and their prices.
def checkout():
    total_price = sum(tea_prices[order.split(' ')[4]] for order in orders)
    order_text = "\n".join(orders) + f"\nTotal Price: ${total_price}"
    messagebox.showinfo("Checkout", order_text)
    orders.clear()

#Label used for Tea Selection.
tea_label = tk.Label(window, text="Tea Selection", font=("Arial", 14))
tea_label.grid(row=0, column=0)
tt_menu = tk.OptionMenu(window, tea_type, *tea_types)
tt_menu.config(height=2, width=20, font=("Arial", 14))
tt_menu.grid(row=0, column=1)
#Label used for Toppings.
topping_label = tk.Label(window, text="Toppings", font=("Arial", 14))
topping_label.grid(row=1, column=0)
topping_menu = tk.OptionMenu(window, topping, *toppings)
topping_menu.config(height=2, width=20, font=("Arial", 14))
topping_menu.grid(row=1, column=1)
#Label used for sugar level.
sugar_label = tk.Label(window, text="Sugar Level", font=("Arial", 14))
sugar_label.grid(row=2, column=0)
sugar_menu = tk.OptionMenu(window, sugar_level, *sugar_levels)
sugar_menu.config(height=2, width=20, font=("Arial", 14))
sugar_menu.grid(row=2, column=1)
#Label used for ice level.
ice_label = tk.Label(window, text="Ice Level", font=("Arial", 14))
ice_label.grid(row=3, column=0)
ice_menu = tk.OptionMenu(window, ice_level, *ice_levels)
ice_menu.config(height=2, width=20, font=("Arial", 14))
ice_menu.grid(row=3, column=1)
#Created the add to order button.
add_button = tk.Button(window, text="Add to Order", command=add_to_order, height=2, width=20, font=("Arial", 14))
add_button.grid(row=4, column=0)
#Created the checkout button.
checkout_button = tk.Button(window, text="Checkout", command=checkout, height=2, width=20, font=("Arial", 14))
checkout_button.grid(row=5, column=0)
# Load and display images for each tea type
for i, tea in enumerate(tea_types):
    img_path = tea_images[tea]  #Opens the image from PIL library
    img = Image.open(img_path)
    img = img.resize((100, 100)) #changes image size
    img_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(window, image=img_tk)
    img_label.image = img_tk 
    img_label.grid(row=i, column=2) 
    price = tk.Label(window, text=tea_prices[tea], font=("Arial", 14)) #Display prices next to each tea
    price.grid(row=i, column=3)
window.mainloop()  #calls the mainloop
