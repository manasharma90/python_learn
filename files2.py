# Read the contents of 'book.txt' and find the most frequent word.
# Hint: Read about split(). 
# Hint: Do not bother if you end up with words such as "Wonderland\n\n". This is acceptable.

with open('book.txt','r') as f:
    a = f.read()            # Reads the contents of the file as a string
  
contents = a.split() # Splits the string contents of the file above to a list with individual words as elements
most_common_word = ""
most_common_count = 0

for x in contents:
    a = contents.count(x)
    if a > most_common_count:
        most_common_count = a
        most_common_word = x
print(most_common_word + ' : ' + str(most_common_count))
 


