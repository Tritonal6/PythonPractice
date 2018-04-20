#! python3

# MultiCB.pyw - The older, better looking brother of clipboard
#
# Usage: py.exe MultiCB.pyw save <keyword> - Saves the clipboard to your specified keyword
#		 py.exe MultiCB.pyw <keyword> - Loads keyword to the clipboard
#		 py.exe MultiCB.pyw list - Loads all existent keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb') # Shelf file creation - prefixed with 'mcb'

# TODO: Save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': # if the cmd is longer than 3 and the first arg is 'save'
# 																(which is ALWAYS index[1] of sys.argv list)
	mcbShelf[sys.argv[2]] = pyperclip.paste() 			 # save contents to the 2nd cmdline argument keyword given
#																(index[2] is the keyword for current clipboard)
elif len(sys.argv) == 2:								 # else if the command is only two args, either error or 'list'
	#TODO: List existing keywords and load their content
	if sys.argv[1].lower() == 'list':					 # if only one argument, is it 'list'? If so:
		pyperclip.copy(str(list(mcbShelf.keys())))		 # copy a string representation of the list of shelf keys to clipb.
#
	elif sys.argv[1].lower() == 'wipe':					 # Now we can completely wipe our list out and start from scratch -
		mcbShelf.clear([sys.argv])						 # Because we're fancy, fancy bois.
#
	elif sys.argv[1] in mcbShelf:						 # otherwise, assume cmdline arg IS a keyword. If this keyword exists:
		pyperclip.copy(mcbShelf[sys.argv[1]])			 # load that key's value to the clipboard.

mcbShelf.close()