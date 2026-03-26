# Inventory System

## Description
This is a simple inventory system made in Python.  
It allows the user to manage products and store data in a CSV file.

## Features
- Add product
- Show inventory
- Find product
- Update product
- Delete product
- Calculate statistics
- Save data to CSV file
- Load data from CSV file

## How it works
The program uses a menu in the console.  
The user selects an option and enters the required data.

The inventory is stored in a list of dictionaries like this:

{
    "product": "rice",
    "price": 2000,
    "quantity": 5
}

## Files in the project
- `app.py` → main program
- `services.py` → inventory functions
- `files.py` → save and load CSV
- `inputs.py` → input validations
