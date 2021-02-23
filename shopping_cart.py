# shopping_cart.py

# import all the modules and third-party packages that we need
from datetime import datetime
import os
from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv


#set the environment vars
load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the package docs for more info
TAX_RATE = os.getenv("TAX_Rate", default=.0875) # uses the os module to read the specified environment variable and store it in a corresponding python variable


# dictionary with products list
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Organic Bananas", "price":.79, "price_per": "pound"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# function to apply currency formatting
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

# capture user input, continue asking for user input until user inputs 'DONE'
selection = []
product_selection = ""
num_products = len(products)

while True:
    product_selection = input("Please input a product identifier, or 'DONE' when finished: ")

    if product_selection.lower() == "done":
        break
    #elif product_selection == "":
       # next
    elif int(product_selection) > num_products:
        print("There is no product with that identifier. Please try again!")
        next
    else:
        for p in products:
            if str(p["id"]) == str(product_selection):
                product_dict = p        
        selection.append(product_dict)
    
    

    # check to see if priced by item or pound
    for p in products:
        if str(p["id"]) == str(product_selection):
            if p["price_per"] == "item":
                next
            else:
                selected_item = p["name"]
                num_pounds = input(f"Please enter the number of pounds of {selected_item}: ")
                selection[len(selection)-1]["price"] = float(selection[len(selection)-1]["price"]) * float(num_pounds)
            

# OUTPUT

# header
print("-------------------------------------")
print("MSB Groceries")
print("msbgroceries.com")
print("-------------------------------------")

# date and time
current_datetime = datetime.now()
current_datetime_str = current_datetime.strftime('%Y-%m-%d %I:%M %p')
print(f"Checkout At: {current_datetime_str}")

# print selected products and capture running total
total = 0

print("-------------------------------------")
for x in selection:
    product_name = x["name"]
    total += float(x["price"])
    product_price = to_usd(x["price"])
    print(f"... {product_name} ({product_price})")
print("-------------------------------------")

# subtotal
total_str = to_usd(total)
print(f"Subtotal: {total_str}")

# tax
tax = TAX_RATE * total
tax_str = to_usd(tax)
tax_rate_str = "{:.2%}".format(TAX_RATE)
print(f"Tax: {tax_str} ({tax_rate_str} tax rate)")

# subtotal
subtotal = total + tax
subtotal_str = to_usd(subtotal)
print(f"Total: {subtotal_str}")

# ending
print("-------------------------------------")
print("Thanks, see you again soon!")
print("-------------------------------------")


# write receipts to file


datetime_receiptfilenamestr = current_datetime.strftime('%Y-%m-%d-%H-%M-%S-%f')

file_name = f"/receipts/{datetime_receiptfilenamestr}.txt" 

with open(file_name, "w") as file:
    # header
    file.write("-------------------------------------")
    file.write("MSB Groceries")
    file.write("msbgroceries.com")
    file.write("-------------------------------------")
    
    # checkout time
    file.write(f"Checkout At: {current_datetime_str}")
    file.write("-------------------------------------")
    
    # products
    for x in selection:
        product_name = x["name"]
        total += float(x["price"])
        product_price = to_usd(x["price"])
        file.write(f"... {product_name} ({product_price})")
    file.write("-------------------------------------")

    # subtotal
    file.write(f"Subtotal: {total_str}")

    # tax
    file.write(f"Tax: {tax_str} ({tax_rate_str} tax rate)")

    # subtotal
    file.write(f"Total: {subtotal_str}")

    # ending
    file.write("-------------------------------------")
    file.write("Thanks, see you again soon!")
    file.write("-------------------------------------")
