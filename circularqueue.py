class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size

        self.front = -1
        self.rear = -1

    def is_empty(self):
        ## Check if queue is empty

        '''
        if  self.queue[self.rear] == None:
            return True

        else:
            return False
        이 if 문도 됨
        '''
        if self.front == -1 and self.rear == -1:
            return True
        elif (self.rear + 1) % self.size == self.front % self.size:
            return True
        else:
            return False

    def is_full(self):
        ## Check if queue is full
        """
        Input:  None
        Output: return True if queue is full
                return False if queue is empty
        """
        if None in self.queue:
            return False
        else:
            return True

    def enqueue(self, item):
        ## Insert an element at the back of the queue
        """
        Input:  item
        Output: print("Cannot Enqueue Full Queue !") if queue is full
        Examples:

            ["Circular", "Queue" ]

            Cannot Enqueue Full Queue !
        """
        if self.is_full():
            print("Cannot Enqueue Full Queue !")

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        ## Remove the element at the front of the queue
        """
        Input:  None
        Output: print("Cannot Remove Empty Queue !") if queue is empty
        Examples:
            ["Circular", "Queue" ]
            >> q.dequeue()
            [None, "Queue" ]
            )
            [None, None ]

            Cannot Remove Empty Queue !
        """
        if self.is_empty():
            print("Cannot Remove Empty Queue !")

        elif self.front == -1:
            self.front = 0
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size

        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size

    def peek(self):
        ## Retrieve the front element of the queue
        """
        Input:  None
        Output: print("No element Empty Queue !") if queue is empty
                return the front element
        Examples:
            ["Circular", "Queue" ]

            Circular


            No element Empty Queue !
        """
        if self.is_empty():
            print("No element Empty Queue !")

        else:
            return self.queue[self.front]

    def display(self):
        ## Completed Funtion - DO NOT REMOVE
        ## Display value(s) of the queue
        if self.is_empty():
            print("Empty Queue !")


        else:
            print(self.queue)


def main():
    queue = CircularQueue(6)
    queue.enqueue("Queue")
    queue.enqueue("is")
    queue.enqueue("simple")
    queue.display()  # Expected Result: ['Queue', 'is', 'simple', None, None, None]

    queue.enqueue("Are")
    queue.enqueue("you")
    queue.enqueue("sure")
    queue.enqueue("?")  # Expected Result: Cannot Enqueue Full Queue !
    queue.display()  # Expected Result: ['Queue', 'is', 'simple', 'Are', 'you', 'sure']

    queue.dequeue()
    print("function peek():", queue.peek())  # Expected Result: function peek(): is
    queue.dequeue()
    queue.display()  # Expected Result: [None, None, 'simple', 'Are', 'you', 'sure']

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    # Expected Result: Cannot Remove Empty Queue !
    queue.peek()  # Expected Result: No element Empty Queue !


main()