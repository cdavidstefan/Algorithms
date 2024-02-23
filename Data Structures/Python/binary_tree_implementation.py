# A binary tree structure allows us to preserve the relationships between the data.
# Pros: Better thank O(n), ordered, flexible size
# Cons: No o(1) operations
# Binary search tree O( log N - lookup, insert, delete )
# Rule 1. All child nodes to the right of the parent node must increase in value,
#         all the child nodes to the left must decrease.
# Rules 2. All nodes must have up to two children.

# Ballanced vs unballanced binary search trees.
# If we only have branches in one direction, it turns into a linked list.
# Why unballanced tree is bad? - optimization, worst case -> o(n)
# How to ballance BST?



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
        else:
            # Value already exists in the tree
            pass

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)


# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

tree.inorder_traversal(tree.root)  # Output: 2 3 4 5 6 7 8
