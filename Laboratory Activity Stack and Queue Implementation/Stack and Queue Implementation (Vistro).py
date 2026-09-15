CAPACITY = 10


class Stack:
    def __init__(self):
        self.items = [None] * CAPACITY
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == CAPACITY - 1

    def push_stack(self, value):
        if self.isFull():
            print("\n[Stack] The stack is full.")
            return

        self.top += 1
        self.items[self.top] = value
        print(f"\n[Stack] Pushed {value} onto the stack.")

    def pop_stack(self):
        if self.isEmpty():
            print("\n[Stack] The stack is empty.")
            return

        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1

        print(f"\n[Stack] Popped {value} from the stack.")

    def peek(self):
        if self.isEmpty():
            print("\n[Stack] The stack is empty.")
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
            print("\n[Stack] is Empty: True")
        else:
            print("\n[Stack] is Empty: False")

    def checkFull(self):
        if self.isFull():
            print("\n[Stack] is Full: True")
        else:
            print("\n[Stack] is Full: False")


class Queue:
    def __init__(self):
        self.data = [None] * CAPACITY
        self.front = 0
        self.rear = -1
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == CAPACITY

    def enqueue_manual(self, value):
        if self.isFull():
            print("\n[Queue] The queue is full.")
            return

        self.rear = (self.rear + 1) % CAPACITY
        self.data[self.rear] = value
        self.count += 1

        print(f"\n[Queue] Enqueued {value} into the queue.")

    def dequeue_manual(self):
        if self.isEmpty():
            print("\n[Queue] The queue is empty.")
            return

        value = self.data[self.front]
        self.data[self.front] = None

        self.front = (self.front + 1) % CAPACITY
        self.count -= 1

        print(f"\n[Queue] Dequeued {value} from the queue.")

    def peek(self):
        if self.isEmpty():
            print("\n[Queue] The queue is empty.")
            return

        print(f"\n[Queue] Front element: {self.data[self.front]}")

    def display(self):
        if self.isEmpty():
            print("\n[Queue] The queue is empty.")
            return

        print("\n[Queue] Contents (Front to Rear):")

        index = self.front
        for _ in range(self.count):
            print(self.data[index])
            index = (index + 1) % CAPACITY

    def checkEmpty(self):
        if self.isEmpty():
            print("\n[Queue] is Empty: True")
        else:
            print("\n[Queue] is Empty: False")

    def checkFull(self):
        if self.isFull():
            print("\n[Queue] is Full: True")
        else:
            print("\n[Queue] is Full: False")


def get_choice():
    try:
        return int(input("Enter choice: "))
    except ValueError:
        return -1


def stack_menu(stack):
    while True:
        print("\n====== STACK MENU ======")
        print("0. Back to Main Menu")
        print("1. Push")
        print("2. Pop")
        print("3. Peek ")
        print("4. Display Stack")
        print("5. Check if Empty")
        print("6. Check if Full")

        choice = get_choice()

        if choice == 1:
            try:
                value = int(input("Enter value to push: "))
                stack.push_stack(value)
            except ValueError:
                print("\nInvalid input, Please try again.")

        elif choice == 2:
            stack.pop_stack()

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
            print("\nInvalid choice, Please try again.")


def queue_menu(queue):
    while True:
        print("\n====== QUEUE MENU ======")
        print("0. Back to Main Menu")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek ")
        print("4. Display Queue")
        print("5. Check if Empty")
        print("6. Check if Full")

        choice = get_choice()

        if choice == 1:
            value = input("Enter value to enqueue: ")
            queue.enqueue(value)

        elif choice == 2:
            queue.dequeue()

        elif choice == 3:
            queue.peek()

        elif choice == 4:
            queue.display()

        elif choice == 5:
            queue.checkEmpty()

        elif choice == 6:
            queue.checkFull()

        elif choice == 0:
            break

        else:
            print("\nInvalid choice, Please try again.")


def main():
    stack = Stack()
    queue = Queue()

    while True:
        print("\n============ MAIN MENU ============")
        print("1. Stack Operations (LIFO)")
        print("2. Queue Operations (FIFO)")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            stack_menu(stack)

        elif choice == "2":
            queue_menu(queue)

        elif choice == "0":
            print("\nExited the menu")
            break

        else:
            print("Invalid choice, Please try again.")


if __name__ == "__main__":
    main()