# A binary tree structure allows us to preserve the relationships between the data.
# Pros: Better than O(n), ordered, flexible size
# Cons: No o(1) operations
# Binary search tree O( log N - lookup, insert, delete )
# Rule 1. All child nodes to the right of the parent node must increase in value,
#         all the child nodes to the left must decrease.
# Rule 2. All nodes must have up to two children.
# Rule 3. Exactly one root.
# Rule 4. Exactly one path between the root and any node


# Balanced vs unbalanced binary search trees.
# If we only have branches in one direction, it turns into a linked list.
# Why unbalanced tree is bad? - optimization, worst case -> o(n)
# How to balance BST?


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         new_node = Node(value)
#         if self.root is None:
#             self.root = new_node
#         else:
#             current_node = self.root
#             while True:
#                 if value < current_node.value:
#                     if not current_node.left:
#                         current_node.left = new_node
#                         return self
#                     current_node = current_node.left
#                 else:
#                     if not current_node.right:
#                         current_node.right = new_node
#                         return self
#                     current_node = current_node.right
#
#     def lookup(self, value):
#         # should simply return the node that we are looking for or null/false...
#         if not self.root:
#             return False
#         current_node = self.root
#         while current_node:
#             if value == current_node.value:
#                 return current_node
#             elif value < current_node.value:
#                 current_node = current_node.left
#             elif value > current_node.value:
#                 current_node = current_node.right
#         return False
#
#     def remove(self, value):
#         if not self.root:
#             return False
#         current_node = self.root
#         parent_node = None
#         while current_node:
#             # traversam copacul pana gasim nodul care trebuie sters
#             if value < current_node.value:
#                 parent_node = current_node
#                 current_node = current_node.left
#             elif value > current_node.value:
#                 parent_node = current_node
#                 current_node = current_node.right
#             elif value == current_node.value:
#                 # We found the node. We have 3 situations:
#
#                 # 1. Node has no right child.
#                 if current_node.right is None:
#                     if parent_node is None:
#                         # Inseamna ca vrem sa stergem nodul radacina. Care are numai left child
#                         self.root = current_node.left
#                     else:
#                         if current_node.value < parent_node.value:
#                             # make the current left child a left child of the parent node
#                             parent_node.left = current_node.left
#                         elif current_node.value > parent_node.value:
#                             # make the current left child a right child of the parent node
#                             parent_node.right = current_node.left
#
#                 # 2. Has a right child which doesn't have a left child.
#                 elif current_node.right.left is None:
#                     if parent_node is None:
#                         self.root = current_node.left
#                     else:
#                         current_node.right.left = current_node.left
#                         if parent_node.value > current_node.value:
#                             # parent > current => make right child of the left the parent
#                             parent_node.left = current_node.right
#                             # parent < current => make right child a right child of the parent
#                         elif parent_node.value < current_node.value:
#                             parent_node.right = current_node.right
#
#                 # 3. Has a right child that has a left child.
#                 else:
#                     # must find right child's leftmost child
#                     leftmost = current_node.right.left
#                     leftmost_parent = current_node.right
#                     while leftmost.left is not None:
#                         leftmost_parent = leftmost
#                         leftmost = leftmost.left
#
#                     # parent's left subtree is now leftmost's right subtree
#                     leftmost_parent.left = leftmost.right
#                     leftmost.left = current_node.left
#                     leftmost.right = current_node.right
#
#                     if parent_node is None:
#                         self.root = leftmost
#                     else:
#                         if parent_node.value > current_node.value:
#                             parent_node.left = leftmost
#                         elif parent_node.value < current_node.value:
#                             parent_node.right = leftmost
#                 return True
#
#     def depth_first_values_iterative(self):
#         if self is None:
#             return []
#
#         stack = [self.root]
#         printed_list = []
#
#         while len(stack) > 0:
#             current_element = stack.pop()
#             print(current_element.value)
#             printed_list.append(current_element.value)
#
#             if current_element.right:
#                 stack.append(current_element.right)
#             if current_element.left:
#                 stack.append(current_element.left)
#
#         print('Nodes values in a list:', printed_list)


# tree = BinarySearchTree()
#
# tree.insert(9)
# tree.insert(4)
# tree.insert(6)
# tree.insert(20)
# tree.insert(170)
# tree.insert(15)
# tree.insert(1)
# tree.insert(200)
# print(tree.remove(20))
# print(tree.lookup(20))
# print(tree)
# print(tree.depth_first_values_iterative())


#           9
#       4       20
#    1    6   15    170


# Look for AVL trees and Red/Black Trees


# Static way representation

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self. left = None
#         self.right = None


# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
#
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

#           a
#          /  \
#         b    c
#        / \    \
#       d   e    f


# Depth First Traversal ##########      ##########    ############    #########     #########

# a -> b we move deeper in the tree before we move laterally -> d -> e -> c -> f
# we go deep until we can't anymore, then we go across.
#
# we use a data structure like a stack
# stack = a
# values = a
# starting from current node (root node), I evaluate it, I see it has two children =>
# I add its children to the stack starting with the right one first,
# to have the left one at the top of the stack (LIFO)
# stack = b / c
# is the stack empty? no => evaluate next one (b) => add e and d to the stack
# stack = c
# values = a, b
# stack = d / e / c
# values = a, b ,d
# stack = e / c
# values = a, b , d, e
# stack = c
# values = a, b, d, e, c
# stack = f
# values = a, b, d , e, c, f
# stack = empty
# this way we check the leftmost branch from the root to the leaf and once we get to the leaf
# we start traversing
# Time complexity is O(n) - traverse the entire stack without checking the same value twice
# Space complexity is O(n) - the only thing we store in memory is the linear data structure, the stack

# 1. Iterative resolving #################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self. left = None
        self.right = None


def depth_first_values_iterative(root):  # root == a in this case and a == Node('a')
    if root is None:
        return []

    stack = [root]
    list_elements = []

    while len(stack) > 0:
        current_element = stack.pop()
        list_elements.append(current_element.data)
        if current_element.right:
            stack.append(current_element.right)
        if current_element.left:
            stack.append(current_element.left)

    print(list_elements)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

depth_first_values_iterative(a)


# 2. Recursive resolving ###################################################################

def depth_first_values_recursive(root):
    # think about the simplest input (null root) -  not just a singular node, a root node.
    if root is None:
        return []

    left_values = depth_first_values_recursive(root.left)  # expected output: [b, d ,e]
    right_values = depth_first_values_recursive(root.right)  # expected output: [c, f]
    # recursive leap of faith

    # characters = ['Yone', 'Yasuo', 'Rammus', 'Mordekaiser', 'Jhin']
    # more_characters = ['Draven', *characters, 'LeBlanc', 'Ahri']
    # print(more_characters)

    node_values = [root.data, *left_values, *right_values]
    return node_values


print('Recursive way:', depth_first_values_recursive(a))


# Breadth first traversal ####################################################################

# instead of a Stack we use a Queue to store the nodes.
# traversam copacul lateral, inainte sa mergem in profunzime.
# last things in queue will be the leafs
# Time complexity is O(n) - we need to check every node, and we don't double-check any node
# Space at worst is O(n) - we add every node into our queue
# O(n) if we assume that adding or removing something to the queue runs in constant time


# Iterative solution ############ # # ##  # ## ## # ##  # # # # # ##################################
def breadth_first_search(root):
    # we can have the queue as a list and use specific methods
    if root is None:
        return []

    queue = [root]
    values = []

    while len(queue) > 0:
        current_node = queue.pop(0)
        # we add them here because the order that we visit the nodes is the order that they leave the queue
        # once something pops, we add its value to the list, to be printed
        values.append(current_node.data)

        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

    print(values)

breadth_first_search(a)