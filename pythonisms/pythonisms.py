import time

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
class LinkedListIterator:
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            value = self.current.value
            self.current = self.current.next
            return value
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        return LinkedListIterator(self.head)      
    
    def __str__(self):
      res = ''
      current = self.head
      while current:
        res += str(current.value) + ', '
        current = current.next
      res = res.strip(', ')

      if len(res):
        return '[' + res + ']'
      else:
        return '[]'

    def add(self, value):
        
        node = Node(value)
        self.size += 1
        
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = node
        
    def __len__(self):
        if self.head is None:
            return 0
        else:
            return(f'The Length of your Linked List is: {self.size}')
    
    def convert(self):
      return tuple(self)

      
    def timer(func):
      pass


    
if __name__ == '__main__':
    ll = LinkedList()
    ll.add('a')
    ll.add('b')
    ll.add('c')
    ll.add('d')
    # print(ll.__len__())
    # for x in ll:
    #   print(x)
    # listcomp = [x for x in ll]
    # print(listcomp)
    # print(ll.convert())
    # print(ll.__repr__())
