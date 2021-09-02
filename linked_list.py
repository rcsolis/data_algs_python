# Simple, double and circular linked list samples.

# Node Class
# Each element in any kind of linked list is a Node.
# Every Node has data, link to the next and to the previous (if apply)

class Node:
    def __init__(self, data, next = None, previous= None) -> None:
        self.data = data
        self.next = next
        self.previous = previous
    
    def __str__(self) -> str:
        return f"Node: {self.data}"

# Standard/Simple linked list
#  Attributes
# Root: points to the beginnig of the list (first Node)
# Size: Total number of Node on the list
#
#  Operations:
#  find(Value): Find if the value exists in the list and retrive it
#  add(Value): Add new node to the list
#  remove(Value): Find if the value exists in the lsit and remove it
#  print(): show all Node values
#
# For adding use the approach to add it to the begining 
#
class LinkedList:
    def __init__(self, root: Node) -> None:
        self._root = root
        self.size  = 1

    def add(self, data)->None:
        new = Node(data, self._root )
        self.size += 1
        self._root = new

    def find(self, data):
        current = self._root
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def remove(self, data):
        
        if self._root.data == data:
            current = self._root
            self._root = current.next
            self.size -= 1
            return current
        
        prev = self._root
        current = self._root.next
        while current is not None:
            if current.data == data:
                prev.next = current.next 
                current.next = None
                self.size -= 1
                return current
            prev = current
            current = current.next
        return None
        
    def __str__(self)->str:
        m = f"LINKED LIST ({self.size}): "
        current = self._root
        while current:
            m+=f" {current} "
            current = current.next
        return m 

# TEST Simple Linked List
print("Standard/Simple Linked List")
first = Node(10,None)
print(f"First Node: {first}")
linked = LinkedList(root=first)
print("Add items")
linked.add(20)
linked.add(30)
linked.add(40)
linked.add(50)
print(linked)
print(f"Current Size: {linked.size}")
res = linked.find(40)
print(f"Searching for '40': {True if res else False}")
res = linked.find(100)
print(f"Searching for '100': {True if res else False}")
res = linked.remove(10)
print(f"REMOVE element '10' {True if res else False}")
print(linked)
res = linked.remove(30)
print(f"REMOVE element '30' {True if res else False}")
print(linked)
res = linked.remove(100)
print(f"REMOVE element '100' {True if res else False}")
print(linked)
res = linked.remove(50)
print(f"REMOVE element '50' {True if res else False}")
print(linked)
print("\n\n")

# Circular Linked List
# Adding elments to the end of the list
class CirciularLinkedList:
    def __init__(self, root: Node) -> None:
        self._root = root
        self._root.next = self._root
        self.size = 1

    def _last(self):
        current = self._root
        while True:
            if current.next == self._root:
                return current
            current = current.next

    def get_root(self):
        return self._root

    def add(self, data)->None:
        if self.size == 0:
            new = Node(data)
            self._root = new
            self._root.next = self._root
        else:
            last = self._last()
            new = Node(data, self._root)
            last.next = new
        self.size+=1

    def find(self, data):
        if self._root.data == data:
            return self._root
        else:
            current = self._root.next
            while current != self._root:
                if current.data == data:
                    return current
                current = current.next
                
            return None
    def remove(self, data):
        if self.size == 0:
            return None
        elif self.size == 1:
            if self._root.data == data:
                current = self._root
                self.size -= 1
                self._root = None
                return current
            else:
                return None
        else:    
            last = self._last()
            current = self._root
            if current.data == data:
                self._root = current.next
                last.next = self._root
                current.next = None
                self.size -= 1
                return current
            prev = self._root
            while current != last:
                if current.data == data:
                    prev.next = current.next
                    current.next = None
                    self.size -= 1 
                    return current
                prev = current
                current = current.next
            
            if current.data != data:
                return None
            prev.next = current.next
            current.next = None
            self.size -= 1
            return current

    def __str__(self)->str:
        m = f"CIRCULAR LINKED LIST ({self.size}): "
        if self.size > 0:
            m+= f" {self._root} ->"
            current = self._root.next
            while current.data != self._root.data:
                m+=f" {current} ->"
                current = current.next
        return m

# Test ciruclar linked list
print("Circular Linked List")
first = Node(10,None)
print(f"First Node: {first}")
clinked = CirciularLinkedList(first)
print(clinked)
res = clinked.remove(10)
print(f"Remove item '10': {True if res else False}")
print(clinked)

print("Add items")
clinked.add(100)
clinked.add(2000)
print(f"Current Size:{clinked.size}")
clinked.add(30000)
clinked.add(400000)
clinked.add(5000000)
print(clinked)
res = clinked.find(30000)
print(f"Searching for '30000': {True if res else False}")
res = clinked.find(12000)
print(f"Searching for '12000': {True if res else False}")
res = clinked.remove(100)
print(f"Remove item '100': {True if res else False}")
print(clinked)
res = clinked.remove(5000000)
print(f"Remove item '5000000': {True if res else False}")
print(clinked)
res = clinked.remove(30000)
print(f"Remove item '30000': {True if res else False}")
print(clinked)
res = clinked.remove(15000)
print(f"Remove item '15000': {True if res else False}")
print(clinked)

clinked.add(30000)
clinked.add(100)
print("TESTING LOOP 10 times OVER CIRCULAR LIST")
my_node = clinked.get_root()
for i in range(10):
    print(my_node, end="->")
    my_node = my_node.next


# Double linked list
# Every node has 3 parts, data, next node and previous node
# Add at the beginning of the list

class DoubleLinkedList:

    def __init__(self, root = None) -> None:
        self._root = root
        self._last = root
        self.size = 1 if root else 0

    def add(self, data):
        if self.size == 0:
            self._root = Node(data, None, None)
            self._last = self._root
        else:
            new = Node(data, self._root, None)
            self._root.previous = new
            self._last = self._root
            self._root = new
        self.size+=1

    def find (self, data):
        if self.size == 0:
            return None
        elif self.size == 1:
            return self._root if self._root.data == data else None
        else:
            current = self._root
            while current is not None:
                if current.data == data:
                    return current
                current = current.next
        return None

    def remove(self, data):
        if self.size == 0:
            return None
        else:
            current = self._root
            while current is not None:
                if current.data == data:
                    if current.previous is None:
                        # root
                        self._root = current.next
                        current.next.previous = None
                        current.next = None
                    elif current.next is None:
                        # last
                        self._last = current.previous
                        current.previous.next = None
                        current.previous = None
                    else:
                        # middle
                        current.next.previous = current.previous
                        current.previous.next = current.next
                        current.next = None 
                        current.previous = None
                    self.size -=1
                    return current
                current = current.next
            return None

    def __str__(self) -> str:
        m = f"DOUBLE LINKED LIST({self.size}): "
        current = self._root
        while current is not None:
            m+= f"<- {str(current)} ->"
            current = current.next
        return m

first = Node(1, None, None)
dlinked = DoubleLinkedList(first)
print("\n\n Double Linked List")
print("Add root")
print(dlinked)
print("add items [2,3,4,5]")
dlinked.add(2)
dlinked.add(3)
dlinked.add(4)
dlinked.add(5)
print(dlinked)
res = dlinked.find(3)
print(f"Searching for '3': {True if res else False}")
res = dlinked.find(4)
print(f"Searching for '4': {True if res else False}")
res = dlinked.find(1)
print(f"Searching for '1': {True if res else False}")
res = dlinked.find(10)
print(f"Searching for '10': {True if res else False}")
res = dlinked.remove(1)
print(f"Remove '1': {res if res else False}")
print(dlinked)
res = dlinked.remove(5)
print(f"Remove '5': {res if res else False}")
print(dlinked)
res = dlinked.remove(3)
print(f"Remove '3': {res if res else False}")
print(dlinked)
