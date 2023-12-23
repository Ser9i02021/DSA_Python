from typing import Union

class Stack():
    # Initializing the stack with an empty vector
    def __init__(self) -> None:
        self.stack = []

    # Push method to insert element on top of the stack
    def push(self, element: Union[int, str]) -> None:
        self.stack.append(element)

    # Pop method to remove and return the element on top of the stack
    def pop(self) -> Union[int, str]:
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        del_element = self.stack[-1]
        del self.stack[-1]
        return del_element
    
    # Top method to return the element on top of the stack
    def top(self) -> Union[int, str]:
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.stack[-1]
    
    # Clear method to empty the stack
    def clear(self) -> None:
        while not self.is_empty():
            del self.stack[-1]         
        

    # Size method to get the quantity of elements in the stack
    def size(self) -> int:
        return len(self.stack)
    
    # Is_empty method to verify if the stack has no elements
    def is_empty(self) -> bool:
        return not len(self.stack)
    
    
# Example usage
my_stack = Stack()

my_stack.push(1)
my_stack.push(3)
my_stack.push(7)

element_on_top_of_stack = my_stack.top()

pop_element = my_stack.pop()

is_stack_empty = my_stack.is_empty()

stack_size = my_stack.size()

my_stack.clear()
