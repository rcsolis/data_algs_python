# Class version of stack
# LIFO: Last in First Out
class Stack:

    def __init__(self):
        self._elements = []
    
    def push(self, item):
        self._elements.append(item)
    
    def pop(self):
        if len(self._elements) > 0:
            return self._elements.pop()
        else:
            return None
    
    def peek(self):
        if len(self._elements) > 0:
            return self._elements[ len(self._elements)-1]
        else:
            return None

    def clear(self):
        self._elements.clear()
    
    def __str__(self) -> str:
        return f"STACK: {self._elements}"


def main():
    stack = Stack()
    
    while True:
        print("""
    
    Stacks in python.
    
    Sample script for demostrate how to Stacks works.

    LIFO: Last In First Out

        Operations:
        1 Push
        2 Pop
        3 Peek
        4 Clear
        5 View
        6 EXIT
    """)
        option = input("Enter your option: ")
        if option.isdigit():
            option = int(option)
            if option == 1:
                print("\n PUSH item:")
                item = input("Enter the item: ")
                stack.push(item)
            elif option == 2:
                print("\n POP item:")
                el = stack.pop()
                print(el)
            elif option == 3:
                print("\n PEEK item:")
                el = stack.peek()
                print(el)
            elif option == 4:
                print("\n Clear stack:")
                stack.clear()
            elif option == 5:
                print("\n Stack Members:")
                print(stack)
            else:
                break
        else:
            print("Incorrect option")
            break


if __name__ == "__main__":
    main()