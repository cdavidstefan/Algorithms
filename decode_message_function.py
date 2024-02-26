# Part 3 - Coding Exercise: Decoding a Message from a Text File
# In this exercise, you will develop a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string.
#
# Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).
#
# Your function must be able to process an input file with the following format:
#
# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you
# In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively, like so:
#
#   1
#  2 3
# 4 5 6
# The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:
#
# 1: I
# 3: love
# 6: computers
# and your function should return the string "I love computers".


def decode(message_file):
    try:
        with open(message_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found!")
        return
    except Exception as e:
        print("An error occurred:", e)
        return

    sorted_dict = None
    dict_obj = {}
    for line in lines:
        try:
            number, word = line.split()
            number = int(number)
            if number in [1, 3, 6, 10, 15]:
                dict_obj[number] = word
                sorted_dict = sorted(dict_obj.items())

        except ValueError:
            print("Invalid format in line:", line.strip())
            continue

    return_value = ""
    for i in range(0, len(sorted_dict)):
        return_value = return_value + " " + sorted_dict[i][1]
        print(sorted_dict[i][0], ":", sorted_dict[i][1])

    print(return_value.lstrip())



    print("Decoded message:",return_value.lstrip())

# Example usage:
decode('encoded_message.txt')
