import requests
import json
from requests.auth import HTTPBasicAuth

# def listing_All_Users():
    
#     BASE_URL=''harbor url''
    
#     # payload = {
#     #     "username": 'a209077',
#     #     "password": 'K8IA7noDWL0f0CN0ForMXBwC1bSt1OVg'
#     # }
    
#     response = requests.get("'harbor url'users",auth=HTTPBasicAuth('a209077','K8IA7noDWL0f0CN0ForMXBwC1bSt1OVg'))
#     #response = requests.post(url=BASE_URL,data=payload)
#     data = response.json()
#     #print('Project Name:',data["name"],'Owner_name:',data["owner_name"])
        
# listing_All_Users()

def listing_All_Users():
{
    url = "'harbor url'users"

    payload = {}
    headers = {
    'Authorization': 'Basic YTIwOTA3NzpLOElBN25vRFdMMGYwQ04wRm9yTVhCd0MxYlN0MU9WZw==',
    'Cookie': 'sid=69644108d9aec319eb552bd7508c796c; _gorilla_csrf=MTY1NzA5MjQ5N3xJalpUV0RWM09WcDFjamRhYjBoeVpGTTNURGxzTmtwWmJGYzRURUZtT0ZGS2RUbE5aR1JTWm5ka1EyczlJZ289fPt7QzZyqy7Tvs4Ljz0H1GypJvdtaaTqQ9V6h8bBJKST'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

}
listing_All_Users

# def get_Specific_User_info():
    
#     user_Id = input("Enter the user_Id")
#    # BASE_URL = "'harbor url'users/"+user_Id
#     BASE_URL=' 'harbor url'users?page=1&page_size=10'
    
#     response = requests.get(f"{BASE_URL}")
#     data = response.json()
#     print('Project Name:',data["name"],'Owner_name:',data["owner_name"])
        
# get_Specific_User_info()


