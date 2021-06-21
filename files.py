# Read in the contents of the file 'hello.txt' and copy them into a new file 'world.txt'
# Hint, lookup `with open` syntax.

with open('hello.txt', 'r') as f:
    a = f.read()

with open('world.txt', 'w') as g:
    g.write(a)

