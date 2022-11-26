from pickle import FALSE, TRUE
from unicodedata import name
from xmlrpc.client import boolean
import requests
import json


def Find_ProjectId():
    BASE_URL = 'harbor url'
    print("listing the projects")
    response = requests.get(f"{BASE_URL}")
   # print(response.json())
    data = response.json()
    project_Name = input("Enter the Project_Name")
    project_found = FALSE 
    for item in data:
     if project_Name == item['name']:
          project_found = TRUE
          break 
     
    if(project_found==TRUE):
          print(item['name']," is alredy exists in the Project List")
    else:
           # Create_Project(item['name'])
            print("Creating a Project is ",item['name'])
            BASE_URL = ''harbor url''
            add_Project = {
                'name' : item['name']
            }
            
            response = requests.post(f"{BASE_URL}/projects", json=add_Project)
            print(response.json())

      
Find_ProjectId()

