import random
words = ['one', 'two', 'three', 'four', 'five']
numbers = []
for i in range(1, len(words) + 1):
    numbers.append(i)
words_dictionary = dict(zip(numbers, words))
help_line = list(words_dictionary.items())
random.shuffle(help_line)
shuffled_dictionary = dict(help_line)

for value in shuffled_dictionary.values(): 
    print(value)