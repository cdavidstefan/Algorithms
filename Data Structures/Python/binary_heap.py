# Every child must have a value smaller that the parent node.
# look-up is O(n) because if we want to find an item on a leaf node for example,
# we must go left and right from the root node.
# In binary search tree we went left or right. -> O(logN)
# Insert and remove are still O(logN)

# They are used a lot in data storage, priority queues, sorting algorithms.
# If we want to find a value larger than some other value we just search the nodes above
# that value. Makes it more efficient

# Heaps add value on the tree in order from left to right.


# Priority queues