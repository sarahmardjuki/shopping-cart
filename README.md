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
```

## Setup: How to Configure Sales Tax Rate for Specific State
Create a new file called ".env" in the root directory of your local repository. 

In the ".env" file, add in the following line of code, replacing the ".08" with your specific tax rate. Make sure you enter the tax rate as a decimal.
```sh
TAX_RATE = .08
```

The program will now update with your specified tax rate.


## Usage

Now you're ready to use the program! Run the Python script from the command-line:
```sh
python shopping_cart.py
```

