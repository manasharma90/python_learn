# Read the contents of 'book.txt' and find the most frequent word.
# Hint: Read about split(). 
# Hint: Do not bother if you end up with words such as "Wonderland\n\n". This is acceptable.

with open('book.txt','r') as f:
    a = f.read()

contents_list = a.split()

from collections import Counter

contents_dict = Counter(contents_list)

word_counts = [("random", 0)]

for k, v in contents_dict.items():
    word_counts.append((k, v))

most_common_word = ''
most_common_count = 0

for i in word_counts:
    if i[1] > most_common_count:
        most_common_word = i[0]
        most_common_count=i[1]

print(most_common_word + ' : ' + str(most_common_count))

