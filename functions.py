# define a function to check if an input string is a palindrome or not
def is_Palindrome(s):
    # if s is a palindrome, return True
    # if s is not a palindrome, return False
    
    forwards_order = []
    for i in s:
        forwards_order.append(i)

    reverse_order = []
    for a in reversed(s):
        reverse_order.append(a)
    
    if forwards_order == reverse_order:
        return True
    else:
        return False

def is_palindrome_new(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-(i+1)]:
            return False
    return True

def is_palindrome_reverse(s):
    return (s == s[::-1])

print(is_palindrome_reverse('malvika'))
print(is_palindrome_reverse('nitin'))
print(is_palindrome_reverse('madam'))
print(is_palindrome_reverse('ntin'))




# define a function to filter even numbers from a given list of numbers
def filter_even(nums):
    filtered = []
    for a in nums:
        if a % 2 == 0:
            filtered.append(a)
    return filtered

test_list = range(100)
print(filter_even(test_list))