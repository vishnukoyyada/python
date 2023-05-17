class Node:
    def __init__(self,data):#creation of just single node not pointing to other nodes
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None#it means  intialy we had a empty linked list,where generelly head points to the first node of linked list
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head#taking the new node(inserted at the begging of the LL)ref as the ref stored in head(which was the actual first node )
        self.head= new_node#after creatinf the new node we are making the add of new node need to be stored in head
    def print_LL(self):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head# n is like a temp
            while n != None:
                print(n.data,"-->",end="")
                n=n.next
    def del_last(self):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head
            while(n.next.next is not None):"""
                                         while loop executes tilln.next.next refers to second_last_node.next means last node
                                        and when it finds latnode.next=None the loop stops
                                        """
                n=n.next
            n.next=None
LL=linkedlist()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)      
LL.del_last()
LL.print_LL()