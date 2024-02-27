# A binary tree structure allows us to preserve the relationships between the data.
# Pros: Better thank O(n), ordered, flexible size
# Cons: No o(1) operations
# Binary search tree O( log N - lookup, insert, delete )
# Rule 1. All child nodes to the right of the parent node must increase in value,
#         all the child nodes to the left must decrease.
# Rules 2. All nodes must have up to two children.
import json


# Ballanced vs unballanced binary search trees.
# If we only have branches in one direction, it turns into a linked list.
# Why unballanced tree is bad? - optimization, worst case -> o(n)
# How to ballance BST?


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        # should simply return the node that we are looking for or null/false...
        if not self.root:
            return False
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
        return False


    def remove(self, value):
        if not self.root:
            return False
        current_node = self.root
        parent_node = None
        while current_node:
            # traversam copacul pana gasim nodul care trebuie sters
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value == current_node.value:
                # We found the node that we want to delete.
                # We have 3 situations:

                # 1. No right child.
                if current_node.right == None:
                    if parent_node == None:
                        # Inseamna ca vrem sa stergem nodul radacina. care are numai left child
                        self.root = current_node.left
                    else:
                        if current_node.value < parent_node.value:
                            # make the current left child a left child of the parent node
                            parent_node.left = current_node.left
                        elif current_node.value > parent_node.value:
                            # make the current left child a right child of the parent node
                            parent_node.right = current_node.left
                # 2. Has a right child which doesn't have a left child.
                elif current_node.right.left == None:
                    if parent_node == None:
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left

                        # parent > current => make right child of the left the parent
                        # va urma...







tree = BinarySearchTree()

tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.lookup(20))
print(tree)


#           9
#       4       20
#    1    6   15    170
