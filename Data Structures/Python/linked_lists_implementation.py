# Hi guys, this is Elon Musk
# and
# This is a linked list with two-way connected nodes:

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length +=1
        return self

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return self

    def insert(self, index, data):
        if index == 0:
            self.append(data)
        else:
            if index > self.length:
                print(f"Index {index} is out of range. I did insert it to the end of the list.")
                return self.append(data)
            new_node = Node(data)
            temporary_tail = self.traverse_to_index(index - 1)

            # * --> * --> * ->
            #    *

            temporary_head = temporary_tail.next
            temporary_tail.next = new_node
            new_node.prev = temporary_tail
            new_node.next = temporary_head
            temporary_head.prev = new_node
            self.length += 1
            return

    def remove(self, index):
        if index == 0:
            self.remove_first_item()
        else:
            if index >= self.length:
                print(f"Index {index} is out of range. Largest index is {self.length - 1}.")
                return

            temporary_tail = self.traverse_to_index(index - 1)
            unwanted_node = temporary_tail.next
            temporary_tail.next = unwanted_node.next
            self.length -= 1
            return

    def remove_last_item(self):
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def remove_first_item(self):
        while self.head:
            new_head = self.head.next
            self.head = new_head
            return

    def remove_everything_after_specified_index(self, index):
        new_tail = self.traverse_to_index(index)
        new_tail.next = None
        return

    def remove_everything_before_specified_index(self, index):
        new_head = self.traverse_to_index(index)
        new_head.prev = None
        self.head = new_head
        return

    def reverse(self):
        if not self.head.next:
            return self

        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return self

    def print_list(self):
        list_data = []
        current_node = self.head
        while current_node is not None:
            list_data.append(current_node.data)
            current_node = current_node.next
        print(list_data)

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while current_node.next is not None and counter != index:
            current_node = current_node.next
            counter += 1
        if current_node is not None:
            return current_node
        else:
            print("index out of range")
        return current_node


myLinkedList = LinkedList(5)
myLinkedList.append(2)
myLinkedList.append(10)
myLinkedList.append(15)
myLinkedList.append(16)
myLinkedList.append(17)
myLinkedList.append(18)
myLinkedList.append(19)
myLinkedList.append(20)
myLinkedList.append(21)
myLinkedList.insert(0, 5)
myLinkedList.remove(0)
myLinkedList.remove_first_item()
myLinkedList.remove_last_item()
myLinkedList.remove_everything_after_specified_index(5)
myLinkedList.remove_everything_before_specified_index(1)


myLinkedList.print_list()

myLinkedList.reverse()

myLinkedList.print_list()