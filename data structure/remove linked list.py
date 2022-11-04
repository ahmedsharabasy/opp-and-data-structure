class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def push(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode

    def deletefirst(self):
        temp=self.head
        self.head=self.head.next
        temp=None  

    def deletelast(self):
        if self.head==None:
            return None
        if self.head.next==None:
            self.head=None
            return None
        secondlast=self.head
        while (secondlast.next.next):    #seconed.next ->last,,seconed.next.next->seconed last
            secondlast=secondlast.next
        secondlast.next=None
        return self.head    

    def deletenode(self,key):
        temp=self.head
        if temp ==None:
            return 
        if temp is not None:
            if temp.data == key:
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev=temp
            temp=temp.next 

        prev.next=temp.next
        temp=None


    def printlist(self):
        temp=self.head
        if temp==None:
            return print('Empty linked list')
        else:    
            print('linked list is:',end=' ')
            while(temp):
                print(temp.data,end='  ')
                temp=temp.next


if __name__=='__main__':
    llist=linkedlist()
    llist.push(10)    
    llist.push(20)                        
    llist.push(30)
    llist.push(40)
    llist.push(50)
    llist.deletelast()
    llist.printlist()
    llist.deletefirst()
    llist.deletenode(20)
    llist.printlist()                        
