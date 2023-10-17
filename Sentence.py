#sentence = "This is a common interview question"
#count = 0
# for char in sentence:
#    number = sentence.count(char)
#    if number > count:
#        count = number
#        highest_char_freq = [char, count]
# print(highest_char_freq)

from pprint import pprint

sentence = "This is a common interview question"


char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)

sorted(frequency.items)
