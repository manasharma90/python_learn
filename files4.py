# Read the contents of 'book.txt' and find the 50 most frequent words.
# Hint: Read about split(). 
# Hint: Do not bother if you end up with words such as "Wonderland\n\n". This is acceptable.

with open('book.txt', 'r') as f:        
    a = f.read()                        

contents_list = a.split()                           # splits the contents of the file into a list form with each word as a separate element

from collections import Counter                     # opening collections module to create a dictionary with words as key and their counts as value

contents_dict = Counter(contents_list)              # dictionary created with words as key and counts as value

word_counts = [('random', 0)]                       # creates a tuple

for k,v in contents_dict.items():                   # loops from the key,value in the dictionary
    word_counts.append((k,v))                       # appends the (key,value) tuple into the list. Now we have a list of tuples with each tuple having a word and its count
 
def sort_tuple(tup):                                # defining a function to sort the tuples by their second element
    tup.sort(key = lambda x: x[1], reverse = True)  # x[1] means the second element in the tuple. reverse is optional- if not written, the list is sorted in ascending order
    return tup

ordered_list = sort_tuple(word_counts)

print(ordered_list[ : 50])                          # printing the first 50 tuples of the list






