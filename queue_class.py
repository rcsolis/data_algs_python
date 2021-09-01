# Class version of Queues
# FIFO : First in First out

class Queue:

    def __init__(self) -> None:
        self._elements = []
    
    def __str__(self) -> str:
        return f"QUEUE: {self._elements}"
    
    def enqueue(self, item) -> None:
        self._elements.append(item)

    def dequeue(self):
        if len(self._elements) > 0:
            return self._elements.pop(0)
        else:
            return None


# Test
myQ = Queue()
myQ.enqueue("Rafael")
myQ.enqueue("Pam")
myQ.enqueue("Emi")
myQ.enqueue("Sofi")

print("My Queue: ")
print(myQ)

el = myQ.dequeue()
print(f"Dequeue: {el}")

print("My Queue: ")
print(myQ)
el = myQ.dequeue()
el = myQ.dequeue()
el = myQ.dequeue()
el = myQ.dequeue()
print(f"Dequeue 4 elements: {el}")

print("My Queue: ")
print(myQ)
