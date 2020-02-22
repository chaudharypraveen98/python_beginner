class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head==None:
            head=Node(data)
            return
        else:
            last_node=head
            while True:
                if last_node.next is None:
                    break
                last_node=last_node.next
            last_node.next=head
        return head
        
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);