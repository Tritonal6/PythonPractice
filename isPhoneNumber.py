#! python3

"""Phone number pattern matching - without using REGEX objects. """

def isPhoneNumber(text):
	if len(text) != 12: # Checks if the string is exactly 12 chars.
		return False
	for i in range(0, 3): # next, we're checking the area code. (first 3 chars in TEXT) consists of nums
		if not text[i].isdecimal():
			return False
	if text[3] != '-': # must have a hyphen after the area code
		return False
	for i in range(4, 7):
		if not text[i].isdecimal(): # numerical check
			return False
	if text[7] != '-': # another hyphen
		return False
	for i in range (8, 12):
		if not text[i].isdecimal(): # numerical check
			return False
	return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
for i in range(len(message)): # we're iterating through the chunk, char by char, checking for pattern
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: ' + chunk)
print('Done')