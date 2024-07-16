# Stack implementation in python

# Creating a stack
def create_stack():
    stack = []
    return stack

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))


# Python program for linked list implementation of stack

# Class to represent a node
class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:

	# Constructor to initialize the root of linked list
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if self.root is None else False

	def push(self, data):
		newNode = StackNode(data)
		newNode.next = self.root
		self.root = newNode
		print ("% d pushed to stack" % (data))

	def pop(self):
		if (self.isEmpty()):
			return float("-inf")
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped

	def peek(self):
		if self.isEmpty():
			return float("-inf")
		return self.root.data


# Driver code
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print ("% d popped from stack" % (stack.pop()))
print ("Top element is % d " % (stack.peek()))


# Trong python không có sự khác biệt giữa stack và các cấu trúc khác
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())

stack.append(5)

if not stack:
    print("Stack is empty!")
else:
    print(f"Stack is not empty, top is: {stack[-1]}")
	