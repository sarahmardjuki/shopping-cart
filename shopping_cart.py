# shopping_cart.py

# import all the modules and third-party packages that we need
from datetime import datetime
import os
from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#set the environment vars
load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the package docs for more info
TAX_RATE = os.getenv("TAX_RATE", default=.0875) # uses the os module to read the specified environment variable and store it in a corresponding python variable
DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
SHEET_NAME = os.getenv("SHEET_NAME", default="products-per-lb")
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google-credentials.json")
AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

## IMPORT PRODUCTS

# authorization
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
client = gspread.authorize(credentials)

# read values

doc = client.open_by_key(DOCUMENT_ID)
sheet = doc.worksheet(SHEET_NAME)
rows = sheet.get_all_records()

products = []
for row in rows:
    products.append(row)



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
    
    for p in products:
        if str(p["id"]) == str(product_selection):
            prodexists = 1
            break
        else: 
            prodexists = 0


    if product_selection.lower() == "done":
        break
    elif prodexists == 0:
        print("There is no product with that identifier. Please try again!")
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
            

## OUTPUT

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
TAX_RATE = float(TAX_RATE)
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

# ask if customer wants an emailed receipt

while True:
    emailreceipt = input("Would the customer like a receipt sent via email? (Yes/No): ")
    if emailreceipt.lower() == "yes" or emailreceipt.lower() == "no":
        break
    else:
        print("Please input either 'Yes' or 'No'.")

if emailreceipt.lower() == "yes":
    emailadd = input("Please input the customer's email address: ")

## write receipts to file

datetime_receiptfilenamestr = current_datetime.strftime('%Y-%m-%d-%H-%M-%S-%f')

file_name = f"receipts/{datetime_receiptfilenamestr}.txt" 
os.makedirs(os.path.dirname(file_name), exist_ok=True)

with open(file_name, "w") as file:
    # header
    file.write("-------------------------------------")
    file.write("\n")
    file.write("MSB Groceries")
    file.write("\n")
    file.write("msbgroceries.com")
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    
    # checkout time
    file.write(f"Checkout At: {current_datetime_str}")
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    
    # products
    for x in selection:
        product_name = x["name"]
        total += float(x["price"])
        product_price = to_usd(x["price"])
        file.write(f"... {product_name} ({product_price})")
        file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")

    # subtotal
    file.write(f"Subtotal: {total_str}")
    file.write("\n")

    # tax
    file.write(f"Tax: {tax_str} ({tax_rate_str} tax rate)")
    file.write("\n")

    # subtotal
    file.write(f"Total: {subtotal_str}")
    file.write("\n")

    # ending
    file.write("-------------------------------------")
    file.write("\n")
    file.write("Thanks, see you again soon!")
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")


## send receipt via email

if emailreceipt.lower() == "yes":
    
    template_data = {
        "total_price_usd": "",
        "human_friendly_timestamp": "",
        "products":[
        ]
    } 

    template_data["total_price_usd"] = subtotal_str
    current_datetime_str2 = current_datetime.strftime('%B %d, %Y %I:%M %p')
    template_data["human_friendly_timestamp"] = current_datetime_str2
    
    for x in selection:
        template_data["products"].append(x)
    

    client = SendGridAPIClient(SENDGRID_API_KEY)

    message = Mail(from_email=SENDER_ADDRESS, to_emails=emailadd)
    message.template_id = SENDGRID_TEMPLATE_ID
    message.dynamic_template_data = template_data

    try:
        response = client.send(message)
 
    except Exception as err:
        print(type(err))
        print(err)

    print("Receipt has been emailed!")


        