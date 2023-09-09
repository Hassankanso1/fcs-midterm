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