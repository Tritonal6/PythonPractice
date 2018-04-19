#! python3

""" A simple Command-line password locker """
# Insecure at best.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
			'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
			'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
	print('Usage: py pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] # first command line arg is the account name.

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to the clipboard.')
else:
	print('There is no account named ' + account)
# This looks into the passwords dictionary for the account name. IF the account name IS a key
## in the dictionary, we get the corresponding value to that key, copy it, and print a confirmation.
### otherwise, we just gaze into the abyss. It's pretty down there.

