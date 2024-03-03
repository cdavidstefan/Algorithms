# A binary tree is a data structure that allows us to preserve the relationships between the data.
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


# Look for AVL trees and Red/Black Trees #####################################################################


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

    print('DFS Iterative way:', list_elements)


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


print('DFS Recursive way:', depth_first_values_recursive(a))


# Breadth first traversal ####################################################################

# instead of a Stack we use a Queue to store the nodes.
# traversam copacul lateral, inainte sa mergem in profunzime.
# last things in queue will be the leafs
# Time complexity is O(n) - we need to check every node, and we don't double-check any node
# Space at worst is O(n) - we add every node into our queue
# O(n) if we assume that adding or removing something to the queue runs in constant time


# Iterative solution ############ # # ##  # ## ## # ##  # # # # # ##################################
# Update: this is the only go to solution when implementing a binary tree bfs traversal
def breadth_first_iterative(root):
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

    return values


print('BFS Iterative way:', breadth_first_iterative(a), '\n')


# def breadth_first_search_recursive(root):
#     if root is None:
#         return []
#
#     left_values = breadth_first_search_recursive(root.left)
#     right_values = breadth_first_search_recursive(root.right)
#
#     node_values = [root.data, *left_values, *right_values]
#     return node_values
#
# print('BFS Recursive way:', breadth_first_search_recursive(a))

# BFS traversal shouldn't be implemented recursively.
# You need a queue in order to traverse a tree "breadth first", and recursion under the hood uses a stack.
# that stack and queue is going to fight against you.
# It can be implemented using recursion by explicitly tracking the level or depth of the nodes being visited
# It is less efficient and can lead to excessive memory usage and stack overflow errors,
# especially for large or deep binary trees.

# Problem 1. Implement the includes method on a binary three. ##################################################
# BFS, iterative.

def includes_bfs_iterative(root, value):
    if root is None:
        return False

    queue = [root]
    node_found = False

    while len(queue) > 0:
        current_node = queue.pop(0)
        print(current_node.data)
        if current_node.data == value:
            return True

        if current_node.left:
            if current_node.left.data == value:
                node_found = True
            queue.append(current_node.left)

        if current_node.right:
            if current_node.right.data == value:
                node_found = True
            queue.append(current_node.right)

    return node_found


value_searched = 'coco jambo'
found_node = includes_bfs_iterative(a, value_searched)
print(f'\nBFS Iterative -> Found node that has value - {value_searched}:', found_node)


# DFS, recursive ##############################################################################################

def includes_dfs_recursive(root, value):
    if root is None:
        return False

    if root.data == value:
        return True

    return includes_dfs_recursive(root.left, value) or includes_dfs_recursive(root.right, value)


print(f'DFS Recursive -> Found node that has value - {value_searched}:', includes_dfs_recursive(a, value_searched))

# Tree Sum     ###########################################################################################


def tree_sum_recursive(root):
    if root is None:
        return 0

    return root.data + tree_sum_recursive(root.left) + tree_sum_recursive(root.right)

# print(tree_sum(some_numeric_value))


# a not so elegant way to write code (it still works!); adding the value of a node as soon as it enters the queue:
def tree_sum_iterative(root):
    if root is None:
        return 0

    total_sum = root.data
    queue = [root]

    while len(queue) > 0:
        current_element = queue.pop(0)
        # total_sum += current_element.data    <-- here we add the value of a node right after it exits the queue

        if current_element.left:
            queue.append(current_element.left)
            total_sum += current_element.left.data  # adding the value as soon as we found a node

        if current_element.right:
            queue.append(current_element.right)
            total_sum += current_element.right.data  # same here

    print(total_sum)

# Min Value of the tree ##############################################################################
# DFS approach

def tree_min_value_dfs(root):
    smallest = float('inf')
    stack = [root]

    while len(stack) > 0:
        current_element = stack.pop()
        if current_element.data < smallest:
            smallest = current_element.data

        if current_element.left:
            stack.append(current_element.left)
        if current_element.right:
            stack.append(current_element.right)

    return smallest


# min_value = tree_min_value(a)
# print('Minimum value inside the tree:', min_value)
# returneaza eroare la linia 440 pentru ca incerc sa compar o litera (valoarea oricarui nod) cu float.

# BFS approach ############################################################################################

def tree_min_value_bfs(root):
    smallest = float('inf')
    queue = [root]

    while len(queue) > 0:
        current_element = queue.pop(0)
        # Python's list implementation (JavaScript as well) uses a dinamically resized c array under the hood.
        # removing elements usually requires to move elements following after, up, to prevent gaps
        # with that said , queue.pop(0) singular runs in O(n)
        if current_element.data < smallest:
            smallest = current_element.data

        if current_element.left:
            queue.append(current_element.left)
        if current_element.right:
            queue.append(current_element.right)

    return smallest
