# Creating an empty queue
# A structure to represent a queue

class Queue:
		# constructor
	def __init__(self, cap):
		self.cap = cap
		self.front = 0
		self.size = 0
		self.rear = cap - 1
		self.arr = [0] * cap

	# Function to create a queue of given capacity
	# It initializes size of queue as 0
	def createQueue(self):
		return Queue(self.cap)
	

class QNode:
	def __init__(self, data):
		self.data = data
		self.next = None


class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
		

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
	
# Function to remove an item from queue.
# It changes front and size

def DeQueue(self):
	if self.isEmpty():
		print("Queue is empty")
		return

	print("% s dequeued from queue" % str(self.Q[self.front]))
	self.front = (self.front + 1) % (self.capacity)
	self.size = self.size - 1
	
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


# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()



from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

while queue:
    print(queue.popleft())
    
if not queue:
    print("Queue is empty!")
	

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Circular Queue implementation in Python

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


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()