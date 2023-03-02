class Node:
    '''
    Node object.
    Args:
        data (str): string value to store in node
    Attributes:
        data (str): value stored in node
        next (Node): pointer to next node in list
    '''
    
    def __init__(self, id:int, name:str, artist: str, album:str):
        self.ID=id
        self.name=name
        self.artist=artist
        self.album=album
        self.next = None
        self.prev= None


    def __repr__(self):
        return '| ID: {} | Name: {} | Artist: {} | Album: {}'.format(self.ID, self.name, self.artist, self.album)


class LinkedList:
    '''
    Linked List object.
    Args:
        None
    Attributes:
        start (Node): pointer to first node in list
    '''

    def __init__(self):
        self.start = None
        self.current=None
        self.length=0


    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.ID +' ' +node.name + ' '+ ' '+ node.artist + ' '+ ' '+ node.album)

        nodes.append("NIL")
        return " --> ".join(nodes)


    def traverse(self):
        '''
        Navigates every node in the list.
        Args:
            None
        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.
        Args:
            None
        Returns:
            None
        '''

        for current_node in self:
            print(current_node)


    def insert_at_beginning(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.
        Args:
            new_node (Node): node to be inserted
        Returns:
            None
        '''
        if self.start== None:
            self.start = new_node
        else:
            self.start.prev=new_node
            new_node.next=self.start
            self.start=new_node
        self.length+=1



    def insert_at_end(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.
        Args:
            new_node (Node): node to be inserted
        Returns:
            None
        '''

        if self.start is None:
            self.start = new_node

        else:
            for current_node in self:
                pass

            new_node.prev=current_node
            current_node.next = new_node
        self.length+=1
            


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.
        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.data == reference_node:
            return self.insert_at_beginning(new_node)
        


        for current_node in self:

            if current_node.data == reference_node:
                
                current_node.prev.next=new_node
                new_node.prev=current_node.prev
                current_node.prev=new_node
                new_node.next = current_node
                self.length+=1
                return
        

        print('Reference node {} not found in linked list...'.format(reference_node))


    def delete(self, reference_node: str):
        '''
        Deletes a node given a value reference.
        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.data == reference_node:
            self.start = self.start.next
            self.length-=1
            return

        for current_node in self:

            if current_node.data == reference_node and current_node.next is not None:
                current_node.prev.next=current_node.next
                current_node.next.prev=current_node.prev
                self.length-=1
                return
            elif current_node.data == reference_node and current_node.next is None:
                current_node.prev.next=current_node.next
                self.length-=1
                return



        print('Reference node {} not found in linked list...'.format(reference_node))
    
    def search(self, search_node):
        for current_node in self:
            if current_node.data == search_node:
                return True
        return False
    
    def play(self):
        if self.start is None:
            print('Playlist is empty')
            return
        if self.current is None:
            self.current=self.start
        print('Now playing ' + str(self.current.name))
    
    def details(self):
        if self.start is None:
            print('Playlist is empty')
            return
        if self.current is None:
            print('No song is playing')
            return
        print(self.current)
    
    def next(self):
        if self.start is None:
            print('Playlist is empty')
            return
        if self.current.next is not None:
            self.current=self.current.next
            print('Now playing ' + str(self.current.name))
            return
        else:
            self.current=self.start
            print('Now playing ' + str(self.current.name)) 
            return
    
    def previous(self):
        if self.start is None:
            print('Playlist is empty')
            return
        if self.current.prev is not None:
            self.current=self.current.prev
            print('Now playing ' + str(self.current.name))
            return
        else:
            print('End of playlist')
    def playlistlen(self):
        if self.start is None:
            print('Playlist is empty')
            return
        print('The playlist has ' + str(self.length) + ' songs')
    
    def playshuffle(self):
        if self.start is None:
            print('Playlist is empty')
            return
        import random
        ran=random.randint(1,self.length)
        temp=self.start
        for i in range(ran-1):
            temp=temp.next
        self.current=temp
        print('Now playing ' + str(self.current.name))

    def searchbyname(self, song: str):
        for current_song in self:
            if current_song.name==song:
                self.current=current_song
                print('Now playing ' + str(self.current.name))
                return
        print('Song has not been found')
        return
    
    def searchbyartist(self, artist: str):
        flag=0
        for current_song in self:
            if current_song.artist==artist:
                flag=1
                print(current_song)
        if flag==0:
            print('No songs found')

    