from queue import CircularQueue
from queue1 import LinearQueue

# Circular Queue instance
queue = CircularQueue(5)
print(queue)

# Enqueues
queue.enqueue('A')
print(queue)
queue.enqueue('B')
print(queue)
queue.enqueue('C')
print(queue)
queue.enqueue('D')
print(queue)
queue.enqueue('E')
print(queue)
queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow
print(queue.peek())
queue.search('B')
# Dequeues
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
queue.enqueue('Z')
print(queue)
queue.dequeue() # Queue Underflow (2nd scenario)

queue_2 = LinearQueue(5)
print(queue_2)
queue.dequeue() # Queue Underflow (1st scenario)

# Linear Queue instance
queue = LinearQueue(5)
print(queue)

# Enqueues
queue.enqueue('A')
print(queue)
queue.enqueue('B')
print(queue)
queue.enqueue('C')
print(queue)
queue.enqueue('D')
print(queue)
queue.enqueue('E')
print(queue)
queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow
print(queue.peek())
queue.search('B')
# Dequeues
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue() # Queue Underflow (2nd scenario)

queue_2 = LinearQueue(5)
print(queue_2)
queue.dequeue() # Queue Underflow (1st scenario)