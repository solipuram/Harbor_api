from pickle import FALSE, TRUE
from unicodedata import name
from xmlrpc.client import boolean
import requests
import json

def listing_Projects():
    BASE_URL = ''harbor url''
    print("listing the projects")
    response = requests.get(f"{BASE_URL}")
   # print(response.json())
    data = response.json()
    for item in data:
      print("Project_Name :",item['name'],"Project_Id :",item['project_id'],"Owner_Name :",item['owner_name'])
         
listing_Projects()




def get_Specific_Project_info():
    
    projet_id = input("Enter the Project_ID")
    BASE_URL = "'harbor url'/"+projet_id
    response = requests.get(f"{BASE_URL}")
    data = response.json()
    print('Project Name:',data["name"],'Owner_name:',data["owner_name"])
        
get_Specific_Project_info()


def is_Projectexists():
    BASE_URL = ''harbor url''
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
          print("Creating a Project is ",item['name'])
          
      
is_Projectexists()
   
   


