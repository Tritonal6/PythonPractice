# This is just a cheat sheet of notes related to the os / os.path module used
## for various functions with the operating system. Linux/OSx/Windows.


# For Windows, it's important to note, that the directory paths are divided by backslashes (\)
# Whereas Linux/OsX are divided by forwardslashes (/)

import os

os.path.join('usr', 'bin', 'spam') 
# >> Prints 'usr\\bin\\spam        --- ( The double backslashes are to escape the previous slash.)

# You can use os.path.join to also create strings of filenames within a list.
myFiles - ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('C:\\Users\\YourName', filename))
# >> C:\\Users\YourName\accounts.txt
# >> C:\\Users\YourName\details.csv
# >> C:\\Users\YourName\invite.docx

# You can even use the os.getcwd() to get the current working directory
os.getcwd()
# >> C:\\Python36

# Even change directories
os.chdir('C:\\Windows\System32')
# >> Now you're in C:\\Windows\\System32

# You might've guessed it- we can create directories too.
os.makedirs('C:\\secretfiles\\supersecretfiles\\totallynotporn')


"""  FIND THE SIZES OF FILES, AS WELL AS CONTENTS OF FOLDERS. """

os.path.getsize(path_here) # returns the size of the file (replaced by path_name) in bytes.

os.listdir(path) # returns a list of filename STRINGS for each file in the path argument.

# If you wanted to get the total size of an entire directory, you can do that by combining both 
## getsize() and listdir() together, with some help from a loop
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'): # You should consider deleting this directory to save a TON of space \s
	totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize) # >> 3129873 bytes 

# With this module, we can also check if paths or files exist. This is huge, because a ton of Python functions end up
## Crashing with errors because you tried supplying them with a path that's not existent.

os.path.exits(path) # returns TRUE if the file or folder placed in the argument exists, and FALSE if not.

os.path.isfile(path) # will return TRUE if the path argument exists and IS a file, otherwise returns FALSE.

os.path.isdir(path) # will return TRUE if the path argument exists and IS a folder, otherwise will return FALSE

# if we were to place these functions into a shell: 
os.path.exists('C:\\Windows')
# >>>>>> True
os.path.exists('C:\\Not_System_32')
# >>>>>> False
os.isdir('C:\\Windows\\System32')
# >>>>>> True
os.isfile('C:\\Windows\\System32')
# >>>>>> False
os.isdir('C:\\Windows\\System32\\calc.exe')
# >>>>>> False
os.path.isfile('C:\\Windows\\System32\\calc.exe')
# >>>>>> True

# You can even check if there's a CD Drive mounted to the system, better yet even a USB Stick.
os.path.exists('D:\\')
# >>>>>> False/True


""" FILE READING AND WRITING """
# Once you become comfortable with dealing with folders and paths, we can then specify the location to read/write.
## The following examples will deal only with PLAINTEXT files for the time being - meaning file extensions with .txt or .py
### If you try opening up a different type of binary file ( term for files whom are confused about their ge- I mean, yeah.)
#### Moving on. If you try to open up other files, you'll see an encoded mess. We'll deal with those later.

""" There's THREE steps to reading or writing files in Python. """
# 1. Call the open() function to return a FILE object.
# 2. Call the read() or write() method ON the FILE object.
# 3. Close the file by calling the close() method ON the FILE object.

"""			OPENING FILES WITH open() 		"""
# In order to open a file with the open() function, we need to pass it a string path, indicating the file we want opened.
## This then returns a FILE object. I've created a .txt document in Documents named secretmessage.txt. In Python IDLE:
secretFile = open('C:\\Users\\Documents\\secretmessage.txt')
# If you're using Linux/OsX:
secretFile = open('/Users/home_folder_here/secretmessage.txt')

# Both of these commands will OPEN the file in 'Read plaintext' mode. This lets you read data from the file, but you can't 
## write or modify the file in any way. This is the default mode, but you can explicitly specify the mode by passing a second
### argument to your open() function like so:
secretFile = open('C:\\Users\\Documents\\secretmessage.txt', 'r')
# This does the same thing as the former.

# By calling open(), this returns a FILE object. This object is stored as a 'value' in python, hence why we stored it in a var

""" READING THE CONTENTS OF FILES """
# now that we have a FILE object, we can start reading from it's contents. If we want to read the entire contents of a file
## as a STRING value, we can use the FILE object's read() method. So, on top of the former code, we'd then call:

secretMessage = secretFile.read() # pass the read() function to a new value, then we'll call that value
secretMessage
# >>>>>>>>>>>> 'wang'			# hah. My message said wang

# Alternatively, we can use the readlines() method to get a LIST of string values. One string for each line of text.

# If we want to WRITE to a file we've opened in read mode - we can't. We need to open it in 'write plaintext' mode, or 
## 'append plaintext'. ('w', 'a') 

# WRITE MODE - Overwrites the existing file and starts from scratch. Just like when we overwrite a variable.
# APPEND MODE - Add's text to the end of the file.

# IF THE FILENAME PASSED TO OPEN() DOESN'T EXIST: Both 'w' and 'a' will create a new blank file.
## Once you're done reading or writing a file, you call the close() method before opening the file once again.
