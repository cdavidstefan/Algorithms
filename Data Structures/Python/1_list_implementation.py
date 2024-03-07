# list slicing in python.
# new_cart = amazon_cart
# this way if we change the value of new cart, the value of amazon cart will change as well
# instead, we can do this: new_cart = amazon_cart[:]
# now only new cart will change
# pointers.

class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def append(self, data):
        self.data[self.length] = data
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def remove(self, index):
        item = self.data[index]
        self.shift_items(index)

        return item

    def remove_everything_after_specified_index(self, index):
        count = 0
        for i in range(index, self.length - 1):
            del self.data[i]
            count += 1
        self.length = self.length - (self.length - count)
        print(self.length)

    def remove_everything_before_specified_index(self, index):
        pass

    def slice_list(self, start_index, end_index, pace):
        pass

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


my_array = Array()
my_array.append('Ana')
my_array.append('are')
my_array.append('mere')
my_array.append('pere')
my_array.append('banane')
my_array.append('!')
my_array.remove_everything_after_specified_index(2)
# broken
print('Length: ', my_array.length)
print('Data: ', my_array.data)
