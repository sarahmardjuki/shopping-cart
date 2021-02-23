# Shopping Cart
The following sections will provide setup instructions and command lines needed to run the program from scratch.

This program will allow the user to enter specific product identifiers during checkout to generate an itemized receipt, with subtotal, tax, and total.  

### Acknowledgments
Based on in class materials from Professor Rossetti. 

## Prerequisites

+ Anaconda 3.7+
+ Python 3.7+
+ Pip

## Setup
Once you have accessed the [repository](https://github.com/sarahmardjuki/shopping-cart) containing the program, fork the remote repository and "clone" your copy onto your computer. 

Navigate to the local repository's root directory, then navigate using the command line:

```sh
cd shopping-cart
```

Use Anaconda to create and activate a new virtual environment. For example, you can call it "shopping-env":

```sh
conda create -n shopping-env python=3.8 
conda activate shopping-env
```

Once you're inside the virtual environment, install the packages before trying to run the program. 

```sh
pip install -r requirements.txt
pip install sendgrid
pip install gspread oauth2client
```

## Setup: How to Configure Sales Tax Rate for Specific State
Create a new file called ".env" in the root directory of your local repository. 

In the ".env" file, add in the following line of code, replacing the ".08" with your specific tax rate. Make sure you enter the tax rate as a decimal.
```sh
TAX_RATE = .08
```

The program will now update with your specified tax rate.

## Setup: Google Sheets API

### Downloading API Credentials
First, go to the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager). Create a new project (or use one you already have), search and enable both the "Google Sheets API" and the "Google Drive API". 

1. Click "Create Credentials," then "Service Account." Name your account (e.g. "spreadsheet-service") and add a role of "Editor".
2. Click the service account you just created under the "Service Accounts" section, and click "Add Key". Then, select "JSON" to create a credentials file. The file should download automatically.
3. Move a copy of the credentials into your project repository, into a new directory called "auth".
4. Add the following code to your ".gitignore" file so the API credentials are not uploaded to GitHub.

```sh
.env
auth/google-credentials.json
```

### Configure the Spreadsheet Document
From here, you have two options. You can use the [example sheet](https://docs.google.com/spreadsheets/d/1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI/edit?pli=1#gid=1279928033), or you can create your own. 

#### Using the Example Sheet
If you choose to use the example sheet, create an environment variable called "GOOGLE_SHEET_ID" and set it equal to the document's identifier (e.g. 1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI). 

#### Using Your Own Sheet
Make sure your file contains column headers id, name, aisle, department, price, and price_per. If you choose to name your sheet anything other than "products-per-lb," create an environment variable called "SHEET_NAME". Finally, change the document's sharing settings to grant "edit" permissions to the "client email" address in the credentials file.

## Setup: How to Configure the Emailed Receipts

### Sending Emails with SendGrid
First, ensure you have or sign up for a [SendGrid account](https://signup.sendgrid.com/). Make sure you confirm your email and verify your account. Complete your "Single Sender Verification" with your desired email. 

Second, create a SendGrid API Key, and click the option for "full access" permissions. Store the API Key in an environment variable called "SENDGRID_API_KEY". 

Third, create an environment variable called "SENDER_ADDRESS" and set it equal to the email address you used during the Single Sender Verification process above. 

### Configuring the Email Template
First, [create a template](https://sendgrid.com/dynamic_templates) with the button in the top right. Copy the template identifier value and store it in an environment value called "SENDGRID_TEMPLATE_ID". 

To customize the email template, copy and paste the following code into the "Code" tab. 

```sh
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello this is your receipt</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<ul>
{{#each products}}
	<li>You ordered: ... {{this.name}}</li>
{{/each}}
</ul>

<p>Total: {{total_price_usd}}</p>
```

You may adjust the formatting of this, but make sure you have some mention of "human_friendly_timestamp", "products", "and "total_price_usd" in your template.



## Check: Environment Variables
The setup process requires many environment variables, if you choose to take all the customization options. See below for a summary of the variables needed:
* TAX_RATE
* GOOGLE_SHEET_ID
* SENDGRID_API_KEY 
* SENDER_ADDRESS 
* SENDGRID_TEMPLATE_ID 

## Usage

Now you're ready to use the program! Run the Python script from the command-line:
```sh
python shopping_cart.py
```

