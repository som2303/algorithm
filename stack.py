class StackNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        ## Check if stack is empty
        """
        Input:  None
        Output: return True if stack is empty
                return False if stack is full
        """
        if self.top is None:
            return True
        else:
            return False

    def push(self, item):
        ## Insert an element at the top of the stack
        """
        Input:  item
        Output: None
        """
        if self.is_empty():
            self.top = StackNode(item)
        else:
            new_node = StackNode(item)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        ## Remove the element from the stack
        """
        Input:  None
        Output: print("Cannot Remove Empty Stack !") if stack is empty
        Examples:
            ["ElementA","ElementB"]
            pop()
            ["ElementA"]
             pop()
            pop()
            Cannot Remove Empty Stack !
        """
        if self.is_empty():
            print("Cannot Remove Empty Stack !")
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.item

    def peek(self):
        ## Completed Funtion - DO NOT REMOVE
        ## Retrieve the first element of the stack
        """
        Input:  None
        Output: print("No element Empty Stack !") if stack is empty
                return the first element of the stack
        """
        if self.is_empty():
            print("No element Empty Stack !")
        else:
            return self.top.item

    def display(self):
        ## Completed Funtion - DO NOT REMOVE
        ## Display value(s) of the stack
        if self.is_empty():
            print("Empty Stack !")
        else:
            cursor = self.top
            nodes = []
            while cursor:
                nodes.append(cursor.item)
                cursor = cursor.next

            print("Stack Values> ", ' -> '.join(nodes))


def main():
    stack = Stack()

    stack.push("Hello")
    stack.display()  # Expected Result: Stack Values>  Hello
    stack.push("Stack")
    stack.push("Last-In First-Out")
    stack.display()  # Expected Result: Stack Values>  Last-In First-Out -> Stack -> Hello

    print("function peek():", stack.peek())  # Expected Result: function peek(): Last-In First-Out

    stack.pop()
    stack.pop()
    stack.display()  # Expected Result: Stack Values>  Hello

    stack.pop()
    stack.display()  # Expected Result: Empty Stack !
    stack.peek()  # Expected Result: No element Empty Stack !
    stack.pop()  # Expected Result: Cannot Remove Empty Stack !


main()