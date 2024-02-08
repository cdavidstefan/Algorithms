class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class LinkedList:
    def __int__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.length +=1
        return self

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.length += 1
        return self

    def print_list(self):
        return None



myLinkedList = LinkedList
LinkedList.append()
print(LinkedList)