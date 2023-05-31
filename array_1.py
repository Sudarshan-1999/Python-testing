# use to stored multiple value in single variable 
# python does not have built-in support for array but python list can be used instead

# File handlling 
# File Handling is important in any application that handles permanent data. We will need file handling if we have to read form or write to files

'''
Open, Read, Write/Create, delete these are the file handling function. 
Open :
    The open() takes two parameters: filename and mode


    syntax : 
    f = open('path to file')

    mode Options:

    'r' Read : The default value ; Open a file for reading; returns an error if the file does not exist
    'a' Append : open a file for appending; create the file if it is not exist
    'w' write: write a file for writing; create the file if it does not exist
    'x' Create: Create the specified file; return an error if a file with the same name already exists.

    
Read :
    The read function is used to read 'n' bytes from the mentioned file
    
    Example: f = open("demofile.txt", "r")
    print(f.read())

    // Reading the first 5 lines
    e.g 
    f = open("demofile.txt","r")
    print(f.read(5))


    // Read line by line
    e.g 
    loop through the file
    f = open("demofile.txt", "r")
    for x in f:
        print(x)



'''

# with Open keyword used for no need to write close function after the file write
with open("sample.txt", 'w') as f:
    f.write("sample line1\nsample line2")

