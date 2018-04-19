#! python3

# PhoneAndEmailExtractor.py - Find phone numbers/emails sitting on the clipboard.


# It's important to think about your program's needs, and plan accordingly, in steps

# This program will need to comply with the following steps:

'''	
+ Get the text off the computer's clipboard.
  - Use the pyperclip module to copy and paste these strings.
+ Find all phone numbers and email addresses held in the copied text.
	- Create two REGEX's:
		- Phone Number REGEX 
		- Email REGEX
	- Find ALL matches; not just the first - of both REGEXes.
	- Neatly format the matched strings into a single string to paste.
	- Display an error message if no matches were found in the selection.
+ Paste them back onto the computer's clipboard to be used accordingly.
'''

import pyperclip, re

# Phone number REGEX pattern
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?								# area code
	(\s|-|\.)?												# hypen or any other separator
	(\d{3})														# three digits following the area code
	(\s|-|\.)?												# hyphen or any other separator
	(\d{4})														# last four digits of the phone number
	(\s*(ext|x|#|ext.)\s*(\d{2,5}))? 	# possible extention - if listed
	)''' re.VERBOSE)

# Email address REGEX pattern
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+					# username
	@													# @ symbol
	[a-zA-Z0-9.-]+						# domain name
	(\.[a-zA-Z]{2,4})					# dot-whatever --- aka top-level domain.
	)''', re.VERBOSE)