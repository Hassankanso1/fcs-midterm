#Q1: Stack and Queues 
class creating_stack_queue:

    def __init__(self):
        self.stack = [] 
        self.queue = []  

    def palindrome(self, info):
        for i in info:
            self.stack.append(i) 
            self.queue.insert(0, i)  
        while self.stack and self.queue:
            if self.stack.pop() != self.queue.pop(0):
                return False 
        return True  
    
def balance(data):
    stack = [] 
    start = "([{"
    end = ")]}"
    for i in data:
        if i in start:
            stack.append(i)
        elif i in end:
            if not stack:
                return False  
            top = stack.pop()  
            if start.index(top) != end.index(i):
                return False 
    return not stack 


input1 = "(1+2)-3*[41+6]"
input2 = "(1+2)-3*[41+6}"
input3 = "(1+2)-3*[41+6"
input4 = "(1+2)-3*]41+6["
input5 = "(1+[2-3]*4{41+6})"
print(balance(input1))  
print(balance(input2)) 
print(balance(input3)) 
print(balance(input4))
print(balance(input5))

#Q2: Cash Wash Exercise
class Car:
    def __init__(self, make, color, plate_number):
        self.make = make
        self.color = color
        self.plate_number = plate_number

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, car):
        self.queue.append(car)
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return len(self.queue) == 0
    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return None

car_wash_queue = Queue()

while True:
    print("Car Wash Queue Program")
    print("1. Insert a car to the queue")
    print("2. Remove the car from the queue")
    print("3. Quit")

    choice = input("Choose your option: ")

    if choice == "1":
        make = input("Enter car make: ")
        color = input("Enter car color: ")
        plate_number = int(input("Enter car plate number: "))
        car = Car(make, color, plate_number)
        car_wash_queue.enqueue(car)
        print(make + " " + color + " (Plate: " + str(plate_number) + ") added to the queue.")

    elif choice == "2":
        if not car_wash_queue.isEmpty():
            removed_car = car_wash_queue.dequeue()
            print("Car removed from the queue:")
            print("Make: " + removed_car.make)
            print("Color: " + removed_car.color)
            print("Plate Number: " + str(removed_car.plate_number))
        else:
            print("No cars in the queue.")

    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid option")
        