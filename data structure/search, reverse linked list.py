class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
            
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev=None
        curr=self.head
        while curr is not None:
            next=curr.next
            curr.next=prev   #عمليه قلب الموشر
            prev=curr
            curr=next
        self.head=prev

    def search(self,item):
        curr=self.head
        while curr !=None:
            if curr.data == item:
                return True
            curr=curr.next
        return False

    def print_search(self,item):
        x=self.search(item)
        if x:
            print('found')
        else:
            print('not found')            
        

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
    llist=LinkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.print_search(10)
    llist.print_search(80)
    llist.printlist()
    llist.reverse()
    llist.printlist() 