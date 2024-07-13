import queue
from collections import deque

# Khởi tạo một queue
# q = queue.Queue()

# # # Thêm các phần tử vào queue
# # q.put(1)
# # q.put(2)
# # q.put(3)

# # Lấy và in ra các phần tử từ queue
# while not q.empty():
#     print(q.get())


# # Khởi tạo một queue sử dụng deque
# q = deque()

# # Thêm các phần tử vào queue
# q.append(1)
# q.append(2)
# q.append(3)

# # Lấy và in ra các phần tử từ queue
# while len(q) > 0:
#     print(q.popleft())


# Ngăn xếp
class Stack:
    def __init__(self):
        self.stack = []
    # Creating a stack
    def create_stack(self):
        return self.stack

    # Creating an empty stack
    def check_empty(self,stack):
        return len(stack) == 0

    # Adding items into the stack
    def push(self,stack, item):
        stack.append(item)
        print("pushed item: " + item)

    # Removing an element from the stack
    def pop(self,stack):
        if (self.check_empty(stack)):
            return "stack is empty"
        return stack.pop()



# Hàng đợi
class Queue:

    def __init__(self,capacity):
        self.queue = []
        self.capacity = capacity
        self.rear = -1  # Khởi tạo rear với giá trị mặc định
        self.Q = [None] * capacity
        self.size = 0

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))



    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    

    # Function to remove an item from queue.
    # It changes front and size

    def DeQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
    
    # Function to get front of queue
    def que_front(self):
        if self.isempty():
            return "Queue is empty"
        return self.Q[self.front]
    
    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.Q[self.rear]
    
    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0
    
    # Queue is full when size becomes
    # equal to the capacity

    def isFull(self):
        return self.size == self.capacity
    

# Hàng đợi dịch vòng
class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()