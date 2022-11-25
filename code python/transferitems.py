class Node:
   def __init__(self , data):
       self.data = data
       self.next = None
class LinkedList:
    def __init__(self):
       self.head = None
    def PrintList(self):
       Lyst = self.head
       print("Items in List are: ")
       while Lyst is not None:
       print(Lyst.data,end=" ")
       Lyst = Lyst.next
    def Update(self , newdata):
       newnode = Node(newdata)
       newnode.next = self.head
       self.head = newnode

Lyst = LinkedList()
lest = [6 , 3 , 2 , 8 , 5 , 7]
n = len(Lest)-1
for i in range(n+1):
   Lyst.Update(Lest[n])
   n = n - 1
Lyst.PrintList()