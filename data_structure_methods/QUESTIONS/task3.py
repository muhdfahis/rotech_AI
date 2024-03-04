import json
import os

employee_data={'count':0,'employee_list':[]}

def create():
    
    name=input("enter the name :")
    age=input("enter your age :")
    phone=input("enter your phone number :")
    exp=input("your experience :")
    grade=input("enter your grade :")
    

    
    employee_data["count"]+=1
    employee_data["employee_list"].append({"name":name,"age":age})
    
    with open("employee.json","w")as file:
        json.dump(employee_data,file)
        
def get():
   
    val=input("enter the name :")
    if os.path.exists("employee.json"):
        with open("employee.json","r+") as file:
            employee_data=json.load(file)  
            
    for emp in employee_data["employee_list"]:
        if emp["name"]==val: 
            for key,value  in emp.items():
                print(key,value)    
    
        
        
while True:
    value=int(input("enter the prompt"))
    
    if value==1:
        create()
        
    if value==2:
        read()
        
    if value==3:
        break