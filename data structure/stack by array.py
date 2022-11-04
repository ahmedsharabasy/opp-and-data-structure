def createstack():
    stack =[]
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,element):
    stack.append(element)
    print(element,'pushed to stack')
    
def poped(stack):
    if isEmpty(stack):
        return print('stack is empty')    
    print( stack.pop(),'poped from stack')

def peek(stack):
    if isEmpty(stack):
        return print('stack is empty')  
    print( stack[len(stack)-1],'is the top value ')   #stack[-1] 


stacck=createstack()
push(stacck,10)
push(stacck,20)
push(stacck,30)
poped(stacck)
peek(stacck)
poped(stacck)
peek(stacck)
poped(stacck)
peek(stacck)
poped(stacck)
peek(stacck)

# class stack:
#     def __init__(self):
#         self.items=[]

#     def isEmpty(self):
#         return self.items==[]

#     def push(self,item):
#         self.items.append(item)
#         print(item,'pushed to stack')

#     def popped(self):
#         if self.isEmpty():
#             return print('Empty stack')
#         print(self.items.pop(),'popped from satck')

#     def peek(self):
#         if self.isEmpty():
#             return print('Empty stack')
#         print(self.items[-1],'is the top value')

# if __name__=="__main__":
#     stack=stack()
#     stack.push(100) 
#     stack.push(200)
#     stack.push(300)
#     stack.push(400)
#     stack.peek()
#     stack.popped() 
#     stack.peek()
#     stack.popped()                                      
#     stack.peek()
#     stack.popped()   
#     stack.peek()
#     stack.popped()   
#     stack.peek()
#     stack.popped()           







    


