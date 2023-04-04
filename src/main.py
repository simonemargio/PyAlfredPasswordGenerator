#!/usr/bin/python3 
import json
import sys
import string
import random

# Gets user's input
myQuery = int(sys.argv[1]) 

def generate_password(length):
    # Define the character set to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the character set
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Generate a password
password = generate_password(myQuery)

#JSON result string for Alfred
result = { "items": [ {
    "title": "Password generated",
    "subtitle": password,
    "valid": 'TRUE',
    "arg": password} 
     ]}     

print (json.dumps(result))