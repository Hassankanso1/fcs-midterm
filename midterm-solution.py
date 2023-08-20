#funnction 1: read data
def uploading():
    data={}
    with open ("database.txt", "r") as f:    
        for line in f: 
            [employee_id, username, timestamp, gender, salary]=line.split(', ') #https://www.freecodecamp.org/news/the-string-strip-method-in-python-explained/
            data[username]={'employee id':employee_id,
                               'timestamp':timestamp,
                               'gender':gender,
                               'salary':int(salary)}
        return data
    
#function 2 : employee Menu defined
def employee_menu(data,username):
    if data[username]["gender"]=="male":
        print("Hi Mr. " + username)
    else:
        print("Hi Ms. " + username)
    print("1. Check my salary")
    print("2. Exit")
    choose=int(input("Choose: "))
    print(choose)
    if choose==1:
        print(data[username]["salary"])

    elif choose==2:
        menu()   

#last funciton: menu display
def menu():
    data=uploading()
    print("cdaoud" in data.values())
    print("Welcome User")
    user=input("enter username: ")
    password=input("enter password: ")
    if user=="admin" and password=="admin123123":
        admin_menu()
    elif user in data.keys():
        employee_menu(data,user)


menu()