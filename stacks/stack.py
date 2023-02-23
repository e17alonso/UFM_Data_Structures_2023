
class Stack:
    '''
    Stack object, array-based implementation.

    Args:
        size (int): size of underlying array

    Attributes:
        elements (List): array of elements
        top (int): pointer at topmost position 
    '''

    def __init__(self, size: int):

        self.MAX=size
        self.elements = [None] * size
        self.top = -1
        
    
    def __repr__(self):
        return 'Current stack: {} | Top: {}'.format(self.elements, self.top)


    def push(self, value: int) -> None:
        '''
        Pushes element into the stack.

        Args:
            value(str): value to be inserted

        Raises:
            RuntimeError: Stack overflow

        Returns:
            None
        '''

        if self.top == self.MAX-1:
            print('Stack overflow')
        else:
            self.top += 1
            self.elements[self.top] = value


    def pop(self) -> int:
        '''
        Pops element out of stack.
        
        Args:
            None

        Raises:
            RuntimeError: Stack underflow

        Returns:
            value (str): value of element popped
        '''

        if self.top == -1:
            print('Stack underflow')
        
        value = self.elements[self.top]
        self.elements[self.top] = None # (Optional)
        self.top -= 1
        return value


    def peek(self) -> int:
        '''
        Peeks topmost element.

        Args:
            None

        Returns:
            value (str): value of element peeked
        '''
        if self.top == -1:
            return 'Stack is empty'
        
        value = self.elements[self.top]
        return value
    
    def search(self, key: int) -> None:
        for i in self.elements:
            if key == self.elements[i]:
                return 'Key has been found'
        return 'Key has not been found'
    

