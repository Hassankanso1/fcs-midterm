#funnction 1: read data
def uploading():
    data={}
    with open ("database.txt", "r") as f:    
        for line in f: 
            [employee_id, username, timestamp, gender, salary]=line.strip().split(',') #https://www.freecodecamp.org/news/the-string-strip-method-in-python-explained/
            data[employee_id]={'username':username,
                               'timestamp':timestamp,
                               'gender':gender,
                               'salary':int(salary)}
        return data
#print(uploading())


#function 2: menu display
def menu():
    print("Welcome User")
    user=input("enter username: ")
    password=input("enter password: ")
    if user=="admin" and password=="admin123123":
        admin_menu()
    elif user in (database) username:
        employee_menu

        
print(menu())