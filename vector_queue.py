from typing import Union

class Queue():
    # Initializing the queue with an empty vector
    def __init__(self) -> None:
        self.queue = []

    # Enqueue method to insert element at the end of the queue
    def enqueue(self, element: Union[int, str]) -> None:
        self.queue.append(element)

    # Dequeue method to remove element at the beginning of the queue
    def dequeue(self) -> Union[int, str]:
        return self.queue.pop(0)
    
    # Back method to return the element at the end of the queue
    def back(self) -> Union[int, str]:
        return self.queue[-1]
    
    # Clear method to empty the queue
    def clear(self) -> None:
        while not self.is_empty():
            self.dequeue()

    # Size method to get the quantity of elements in the queue
    def size(self) -> int:
        return len(self.queue)
    
    # Is_empty method to verify if the queue has no elements
    def is_empty(self) -> bool:
        return not len(self.queue)
    

# Example usage
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(7)

element_on_back_of_queue = my_queue.back()

pop_first_element_of_queue = my_queue.dequeue()

is_queue_empty = my_queue.is_empty()

queue_size = my_queue.size()

my_queue.clear()
