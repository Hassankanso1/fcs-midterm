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
    if choose==1:
        print(data[username]["salary"])
        employee_menu(data,username)

    elif choose==2:
        menu()   


#function 3: Display statistics:
def statistics(data):
    male=0
    female=0
    
    for i in data.keys():
        if i["gender"]=="male":
            male += 1
        if i["gender"]=="female":
            female += 1
    total=male+female
    male_=(male/total)*100
    female_=(female/total)*100
    print(male_,female_)

#function 4 to add employee

#function 5 to display all employees
def display_all(data):
     sorting_employees = sorted(data.values(), key=lambda x: x["timestamp"])    #https://stackoverflow.com/questions/62810058/python-is-there-a-way-to-sort-a-list-of-strings-which-contain-a-date-and-time-w
     for i in sorting_employees:
        print("employee id:", i['employee id'])
        print("timestamp:", i['timestamp'])
        print("gender:", i['gender'])
        print("salary:", i['salary'])
    


#function 6 to change employee's salary

#function 7 to remove employee

#function 8 to increase salary

#function 9 to exit



#function 10: admin menu defined
def admin_menu():
    data=uploading()
    print("1. Dispaly Statistics")
    print("2. Add an Employee")
    print("3. Display all employees")
    print("4. Change employee's salary")
    print("5. Remove employee")
    print("6. Raise employee's salary")
    print("7. Exit")

    choose=int(input("Choose: "))
    
    if choose==1:
        statistics(data)
        admin_menu()
    elif choose==2:
        add_employee()
        admin_menu()
    elif choose==3:
        display_all(data)
        admin_menu()
    elif choose==4:
        change_salary()
        admin_menu()
    elif choose==5:
        remove_employee()
        admin_menu()
    elif choose==6:
        increase_salary()
        admin_menu()
    elif choose==7:
        menu()
    elif choose<1 or choose >7:
        print("Choose again")
        admin_menu()
    
        
    

#function 11: menu display
def menu():
    verification=False
    iterator=1
    data=uploading()
    #print("cdaoud" in data.values())


    while iterator<=5 and verification == False:

        print("Welcome User")
        user=input("enter username: ")
        password=input("enter password: ")

        if user=="admin" and password=="admin123123" :
            admin_menu()
            verification=True

        elif user in data.keys():
            employee_menu(data,user)
            verification=True

        else:
            print("Try again")
            iterator+=1

    if iterator==5:
        print('5 Trials')
        return


menu()