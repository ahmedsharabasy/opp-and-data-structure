class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class CircularLinkedList:        
    def __init__(self):
        self.last=None

    def addtoEmpty(self,item):
        if self.last !=None:
            return self.last
        newnode=Node(item) 
        self.last=newnode
        newnode.next=self.last.next  #ربط النودات ببعض circular
        return self.last

    def addbegain(self,item):
        if self.last==None:
            return self.addtoEmpty(item)
        newnode=Node(item)
        newnode.next=self.last.next
        self.last.next=newnode
        return self.last

    def addEnd(self,item):
        if self.last==None:
            return self.addtoEmpty(item)               
        newnode=Node(item)
        newnode.next=self.last.next
        self.last.next=newnode
        newnode=self.last
        return self.last

    def addafter(self,data,item):
        if (self.last == None):
            return None
        newnode=Node(item)   
        p=self.last.next
        while p:
            if (self.last == None):
                return None
 
        temp = Node(data)
        p = self.last.next
        while p:
            if (p.data == item):
                temp.next = p.next
                p.next = temp
 
                if (p == self.last):
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next
            if (p == self.last.next):
                print(item, "not present in the list")
                break
 
    def traverse(self):
        if (self.last == None):
            print("List is empty")
            return
 
        temp = self.last.next
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
            if temp == self.last.next:
                break

if __name__ == '__main__':
 
    llist = CircularLinkedList()
 
    last = llist.addToEmpty(6)
    last = llist.addBegin(4)
    last = llist.addBegin(2)
    last = llist.addEnd(8)
    last = llist.addEnd(12)
    last = llist.addAfter(10,8)
 
    llist.traverse()            


