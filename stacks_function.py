# functional version of stack
stack = [];

def main():
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
                push()
            elif option == 2:
                pop()
            elif option == 3:
                peek()
            elif option == 4:
                clear()
            elif option == 5:
                view()
            else:
                break
        else:
            print("Incorrect option")
            break

def view():
    print("\n View elements:")
    print(stack)

def push():
    print("\n")
    member = input("Enter the element:")
    print("Always push on top.")
    print("before:", stack)
    stack.insert(0, member)
    print("after:", stack)

def pop():
    print("\nAlways pop from top (modify the stack).")
    print("before:", stack)
    el = stack.pop(0)
    print(f"POPPED ELEMENT {el}")
    print("after:", stack)

def peek():
    print("\nAlways peek from top (NOT modify the stack).")
    print("before:", stack)
    el = stack[0]
    print(f"PEEKED ELEMENT {el}")
    print("after:", stack)

def clear():
    print("Clear the stack")
    print("before:", stack)
    stack.clear()
    print("after:", stack)


if __name__ == "__main__":
    main()