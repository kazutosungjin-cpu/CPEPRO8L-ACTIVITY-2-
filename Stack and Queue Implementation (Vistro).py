CAPACITY = 10


class Stack:
    def __init__(self):
        # Fixed-size list
        self.items = [None] * CAPACITY
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == CAPACITY - 1

    def push(self, value):
        if self.isFull():
            print("\n[Stack] Overflow! The stack is full.")
            return

        self.top += 1
        self.items[self.top] = value
        print(f"\n[Stack] Pushed {value} onto the stack.")

    def pop(self):
        if self.isEmpty():
            print("\n[Stack] Underflow! The stack is empty.")
            return

        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1

        print(f"\n[Stack] Popped {value} from the stack.")

    def peek(self):
        if self.isEmpty():
            print("\n[Stack] Underflow! The stack is empty.")
            return

        print(f"\n[Stack] Top element: {self.items[self.top]}")

    def display(self):
        if self.isEmpty():
            print("\n[Stack] Stack is empty.")
            return

        print("\n[Stack] Contents (Top to Bottom):")

        for i in range(self.top, -1, -1):
            print(self.items[i])

    def checkEmpty(self):
        if self.isEmpty():
            print("\n[Stack] isEmpty: True")
        else:
            print("\n[Stack] isEmpty: False")

    def checkFull(self):
        if self.isFull():
            print("\n[Stack] isFull: True")
        else:
            print("\n[Stack] isFull: False")







operations = []
x = []


  def main():

    stack = Stack()
    queue = Queue()

    while True:
        print("\n")
        print("=== Main Menu ===")
        print("1. Stack Operations (LIFO)")
        print("2. Queue Operations (FIFO)")
        print("0. Exit")
  
  def stack_menu(stack):

    while True:
        print("\n")
        print("--------- STACK MENU ---------")
        print("1. Push")
        print("2. Pop")
        print("3. Peek (Top)")
        print("4. Display Stack")
        print("5. Check if Empty")
        print("6. Check if Full")
        print("0. Back to Main Menu")

        choice = get_choice()

        if choice == 1:
            try:
                value = int(input("Enter value to push: "))
                stack.push(value)
            except ValueError:
                print("\nInvalid input! Please enter a number.")

        elif choice == 2:
            stack.pop()

        elif choice == 3:
            stack.peek()

        elif choice == 4:
            stack.display()

        elif choice == 5:
            stack.checkEmpty()

        elif choice == 6:
            stack.checkFull()

        elif choice == 0:
            break

        else:
            print("\nInvalid choice! Please select from the menu.")

  def stack_menu(stack):
    
    while True:
        print("\n")
        print("---Queue Menu---")
        print("0. Back to menu")
        print("1. Enqueue")
        print("2. Disqueue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Check if empty")
        print("6. Check if full")
        choice = input ("Choice (0-6):")


        if choice == "3":
          print("Exit Menu")
          break