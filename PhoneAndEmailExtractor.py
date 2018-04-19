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
	(\s*(ext|x|ext.)\s*(\d{2,5}))? 		# possible extention - if listed
	)''', re.VERBOSE)

# Email address REGEX pattern
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+					# username
	@													# @ symbol
	[a-zA-Z0-9.-]+						# domain name
	(\.[a-zA-Z]{2,4})					# dot-whatever --- aka top-level domain.
	)''', re.VERBOSE)

# Time to crawl that clipboard
text = str(pyperclip.paste())			# take the copied text from clipboard, give it a home.. a text home.
matches = []											# create an empty list, give it to matches. Matches likes empty lists.

for groups in phoneRegex.findall(text):			# iterate through the groups created by the phoneRegex.compile()
	phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # join each tuple grouping with the '-'  \(-.-\)
	if groups[8] != '':												# we do this, so we can build our perfect phone number structure
		phoneNum += ' x' + groups[8]						# not because we HAVE TO....  but because we... no we have to
	matches.append(phoneNum)									# add these matches to our list of them sweet, sweet deets

for groups in emailRegex.findall(text): # iterate through all groups created by the emailRegex.compile()
	matches.append(groups[0])	# for each match, append it to group 0.

# By now, matches has a nice big list of emails and phone numbers. But as I said, matches likes empty lists.
## Time to put those values back where they belong.

if len(matches) > 0: 	# if the length of our matches list is greater than 0 - 
	pyperclip.copy('\n'.join(matches))	# copy everything to our System's clipboard
	print('Copied to clipboard: ') 			# tell that to our users, because they like to be in the know
	print('\n'.join(matches))						# show them what we found and copied, because 'something' killed the cat
else:																	# otherwise, if our list IS empty, our clipboard was probably empty
	print('I feel like you might be missing something...')