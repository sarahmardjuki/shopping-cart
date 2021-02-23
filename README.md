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
```

## Setup: How to Configure Sales Tax Rate for Specific State
Create a new file called ".env" in the root directory of your local repository. 

In the ".env" file, add in the following line of code, replacing the ".08" with your specific tax rate. Make sure you enter the tax rate as a decimal.
```sh
TAX_RATE = .08
```

The program will now update with your specified tax rate.

## Setup: How to Configure the Emailed Receipts

### Sending Emails with SendGrid
First, ensure you have or sign up for a [SendGrid account](https://signup.sendgrid.com/). Make sure you confirm your email and verify your account. Complete your "Single Sender Verification" with your desired email. 

Second, create a SendGrid API Key, and click the option for "full access" permissions. Store the API Key in an environment variable called "SENDGRID_API_KEY". 

Third, create an environment variable called "SENDER_ADDRESS" and set it equal to the email address you used during the Single Sender Verification process above. 

## Configuring the Email Template
First, [create a template](https://sendgrid.com/dynamic_templates) with the button in the top right. Copy the template identifier value and store it in an environment value called "SENDGRID_TEMPLATE_ID". 

To customize the email template, copy and paste the following code into the "Code" tab. 

'''sh
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello this is your receipt</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<ul>
{{#each products}}
	<li>You ordered: ... {{this.name}}</li>
{{/each}}
</ul>

<p>Total: {{total_price_usd}}</p>
'''

You may adjust the formatting of this, but make sure you have some mention of "human_friendly_timestamp", "products", "and "total_price_usd" in your template.

## Usage

Now you're ready to use the program! Run the Python script from the command-line:
```sh
python shopping_cart.py
```

