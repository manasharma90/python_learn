# This is a comment

numbers = [1,2,3,4,5,6,7]

# Step 1
# Add more numbers to this list till you reach 10

more_numbers = [8,9,10]
numbers = numbers + more_numbers

# Step 2
# Eliminate all Odd numbers from the list

for n in numbers:
    if n % 2 != 0:
        numbers.remove(n)

# Step 3
# Multiply all the elements in the list by 5

x = len(numbers)

for i in range(x):
    numbers[i] = numbers[i] * 5

print(numbers)


# Step 4 - Verify
assert(numbers == [10, 20, 30, 40, 50])