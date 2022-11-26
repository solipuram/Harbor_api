from pickle import FALSE, TRUE
from unicodedata import name
from xmlrpc.client import boolean
import requests
import json

def listing_users():
    BASE_URL = 'harbor url'
    print("listing the projects")
    response = requests.get(f"{BASE_URL}")
   # print(response.json())
    data = response.json()
    for item in data:
      print("Username :",item['username'],"State :",item['state'])
         
listing_users()
