class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_last(self, item):
        new_node = Node(item)
        temp = self.head
        if self.is_empty():
            self.head = new_node
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        # Add a value in the end of the list

    def add_first(self, item):
        ## Completed Function - Do not remove
        # Add a value in the begin of the list
        new_node = Node(item)
        if not self.is_empty():
            new_node.next = self.head
        self.head = new_node

    def add(self, pos, item):
        # Add a value in the 'pos' position of the list
        # Ex.   linked list values>  3 -> 7 -> 4
        #       >>> add(2, 5)
        #       linked list values>  3 -> 5 -> 7 -> 4
        if self.get_length() < pos:
            print('index out of range')
        else:
            start_node = self.head
            for i in range(pos - 2):
                start_node = start_node.next
            print(start_node.value)
            new_node = Node(item)
            new_node.next = start_node.next
            start_node.next = new_node

    def delete_last(self):
        # Delete a value in the end of the list
        temp = self.head

        if self.get_length() == 1:
            self.head = None

        else:
            if self.is_empty():
                temp = None
            else:
                while temp.next != None:
                    pre = temp
                    temp = temp.next
                pre.next = None

    def delete_first(self):
        # Delete a value in the begin of the list
        temp = self.head
        if temp.next == None:
            self.head = None
        else:
            self.head = temp.next

    def display(self):
        ## Completed Function - Do not remove
        # Display value(s) of the list
        if self.is_empty():
            print("linked list is empty !!")

        else:
            values = []

            start_node = self.head
            while start_node:
                values.append(start_node.value)
                start_node = start_node.next

            print("linked list values> ", ' -> '.join(map(str, values)))

    def get_length(self):
        # Get length of the list
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
        # Check if the list is empty


def main():
    linked_list = LinkedList()

    linked_list.add_last(3)
    linked_list.add_last(7)
    linked_list.add_last(4)
    linked_list.display()  # Expected Result: linked list values>  3 -> 7 -> 4

    linked_list.add_first(1)
    linked_list.add_first(2)
    linked_list.display()  # Expected Result: linked list values>  2 -> 1 -> 3 -> 7 -> 4

    linked_list.add(7, 100)  # Expected Result: list position out of range !!

    linked_list.add(3, 100)
    linked_list.display()  # Expected Result: linked list values>  2 -> 1 -> 100 -> 3 -> 7 -> 4

    linked_list.delete_first()
    linked_list.display()
    linked_list.delete_last()
    linked_list.display()  # Expected Result: linked list values>  1 -> 100 -> 3 -> 7

    linked_list.delete_first()
    linked_list.delete_last()
    linked_list.delete_first()
    linked_list.display()  # Expected Result: linked list values>  3

    linked_list.delete_last()
    linked_list.display()  # Expected Result: linked list is empty !!


main()