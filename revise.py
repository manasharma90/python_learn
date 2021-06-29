#!/usr/bin/env python3
# Your task is to find all the palindromes in the support_files/words_alpha.txt file.
# This file contains thousands of english words, your program needs to create a list of all the palindromes within this list.


import sys



# First function is to read the file and create a list of words from the file
def read_words(filename):
    with open(filename, 'r') as f:
        a = f.read()
    words = a.split()                   # splits the contents of the file into a list form with each word as a separate element
    return words     


# Second function is to check if any word is a palindrome       
def is_palindrome(word):
    for i in range(len(word)):          # checks letter-wise within the range of the length of the word
        if word[i] != word[len(word)-(i+1)]:
            return False
    return True
    

# Third function checks a list of words for palindromes and returns a set of unique palidromes in the list, using the second function
def find_palindromes(words):  
    palindromes = set()                 # generates a set so that only unique words are included in the final count
    for i in words:
        if is_palindrome(i):            # default is == True; if False needs to be added, then use: if is_palindrome(i) == False:
            palindromes.add(i.lower())  # Using lowercase only because upper and lower case are considered unique in the set.
    return palindromes


# This is the main function of your program.
def main(filename):
    words = read_words(filename)            # runs the first function from above
    palindromes = find_palindromes(words)   # runs the third function 
    print("Found " + str(len(palindromes)) + " palindromes.")
    print(list(palindromes)[:5])

# This is boilerplate code to call the main function when this script is run.
if __name__=="__main__":
    main(sys.argv[1])