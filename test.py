#file = open("database.txt", "r")
#x=f.readline(1)
#print(x)

#with open("database.txt", "r") as f:
#    print(f.readline())
#    print(f.readline())

#with open("database.txt", "r") as f:
#    print(f.readlines(1))



#funnction 1: read data
def uploading(data):
    data={}
    with open ("database.txt", "r") as f:    #https://www.youtube.com/watch?v=2dUu7r14JwM
        for line in f: 
            employee_id, username, timestamp, gender, salary=line.strip().split(',')
            data[employee_id]={'username'=username,'timestamp'=timestamp,'gender'=gender,'salary'=int(salary)}
        return data
    

