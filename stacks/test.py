from stack import Stack

# Stack initialization
stack = Stack(10)
print(stack)

# Push first element
stack.push(1)

# Other pushes
stack.push(2)
print(stack)
stack.push(3)
print(stack)
stack.push(4)
print(stack)
stack.push(5)
print(stack)
stack.push(6)
print(stack)
stack.push(7)
print(stack)
stack.push(8)
print(stack)
stack.push(9)
print(stack)
stack.push(10)
print(stack)

stack.push(11)
print(stack)
# stack.push('F') # Forces stack overflow

stack.search(8)
# Pops
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
# stack.pop() # Forces stack underflow

# Peek
stack.push('4')
stack.push('3')
print(stack)
print('Peek: ', stack.peek())
stack.push('5')
print(stack)
print('Peek: ', stack.peek())

from stack import Stack


original_list = [1, 33, 14, 16, 77, 55, 11, 4, 23, 24]
print('Original list:', original_list)
stack = Stack(10)

for element in original_list:
    stack.push(element)
    print(stack)

reversed_list = []

while stack.peek() != 'Stack is empty':
    reversed_list.append(stack.pop())
    print(stack)
    print(reversed_list)

print('Reversed list:', reversed_list)
