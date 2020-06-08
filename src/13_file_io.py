"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os
reader = open('src/foo.txt', 'r')
try:
    # stuff
    for line in reader:
        print(line, end="")
finally:
    reader.close
    print('End of file')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain


# YOUR CODE HERE
bar_file = 'src/bar.txt'

if os.path.exists(bar_file):
    append_write = 'a'
else:
    append_write = 'w'

writer = open(bar_file, append_write)

try:
    writer.write(input("Write some stuff! ") + '\n')
finally:
    writer.close()
