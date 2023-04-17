from playlist import Node, LinkedList


# Nodes instantiation
node_a = Node('1', 'Moscow Mule', 'Bad Bunny', 'Un Verano sin ti')
node_b = Node('2', 'Dime Quien???', 'Rauw Alejando', 'Saturno')
node_c = Node('3', 'Close Friends', 'Alvaro Diaz', 'Felicilandia')
node_d= Node('4', 'Feliz cumpleaños Ferxxo', 'Feid', 'Feliz cumpleaños Ferxxo')


# Create LL
ll = LinkedList()
print(ll)

ll.insert_at_beginning(node_c)
print(ll)
ll.insert_at_beginning(node_b)
print(ll)
ll.insert_at_beginning(node_a)
print(ll)
ll.insert_at_end(node_d)
print(ll)

ll.play()
ll.details()
ll.next()
ll.previous()
ll.previous()
ll.playlistlen()
ll.playshuffle()
ll.searchbyname('Moscow Mule')
ll.searchbyartist('Alvaro Diaz')