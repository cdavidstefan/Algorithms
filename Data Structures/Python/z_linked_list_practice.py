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
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, data):
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
        elif index >= self.length:
            print(f"Index of {index} is out of range. I did append the item at the end of the list.")
            self.append(data)
        else:
            new_node = Node(data)
            temporary_tail = self.traverse_to_index(index - 1)
            temporary_head = temporary_tail.next
            temporary_tail.next = new_node
            new_node.prev = temporary_tail
            new_node.next = temporary_head
            temporary_head.prev = new_node
            self.length += 1
            return self

    def remove(self, index):
        if index == 0:
            self.remove_first_item()
        elif index > self.length:
            print(f"You want to remove a node with an index that's out of range. I will remove last node.")
            temporary_tail = self.tail.prev
            self.tail = temporary_tail
            self.length -= 1
            return self
        else:
            temporary_tail = self.traverse_to_index(index - 1)
            unwanted_node = temporary_tail.next
            temporary_tail.next = unwanted_node.next
            self.length -= 1
            return self

    def remove_first_item(self):
        while self.head:
            self.head = self.head.next
            self.length -= 1
            return self

    def remove_last_item(self):
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def remove_everything_after_specified_index(self, index):
        temporary_tail = self.traverse_to_index(index)
        temporary_tail.next = None
        self.tail = temporary_tail
        self.length = self.length - (self.length - index) + 1

    def remove_everything_before_specified_index(self, index):
        self.head = self.traverse_to_index(index)
        self.length -= index

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
        list_values = []
        current_element = self.head

        while current_element is not None:
            list_values.append(current_element.data)
            current_element = current_element.next

        return list_values

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head

        while current_node is not None and counter != index:
            current_node = current_node.next
            counter += 1
        if current_node is not None:
            return current_node
        else:
            print("Index out of range!")
        return current_node


myLinkedList = LinkedList('A')
myLinkedList.append('n')
myLinkedList.append('a')
myLinkedList.append(' ')
myLinkedList.append('a')
myLinkedList.append('r')
myLinkedList.append('e')
myLinkedList.append(' ')
myLinkedList.append('m')
myLinkedList.append('e')
myLinkedList.append('r')
myLinkedList.append('e')
myLinkedList.append('.')
myLinkedList.insert(1, 'a')
myLinkedList.insert(1, 'a')
myLinkedList.insert(2, 'a')
myLinkedList.insert(2, 'a')
myLinkedList.insert(2, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')
myLinkedList.insert(7, 'a')

print(myLinkedList.print_list())
arr_letters = myLinkedList.print_list()
sentence = "".join(str(x) for x in arr_letters)
print(sentence)

print(myLinkedList.traverse_to_index(0).data)

# print(myLinkedList.length)
# myLinkedList.remove_everything_after_specified_index(2)
# print(myLinkedList.length)
# myLinkedList.remove_everything_before_specified_index(4)
# print(myLinkedList.length)

myLinkedList.reverse()
# why is this not working?

print(myLinkedList.print_list())
arr_letters = myLinkedList.print_list()
sentence = "".join(str(x) for x in arr_letters)
print(sentence)

print(myLinkedList.traverse_to_index(0).data)
