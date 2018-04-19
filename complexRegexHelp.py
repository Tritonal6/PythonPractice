# This is simply just a reference file for how to handle complex REGEX

import re

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# Let's clean that shit up. 

phoneRegex = re.compile(r'''( # The triple quote allows a multi-line string to make the REGEX more legible
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE) # This VERBOSE argument tells the compiler to IGNORE the whitespace inside the compilefunction

# Additionally, here's a small table with commonly used REGEX character classes
character_classes = {
	'\d' : 'Any numeic digit 0-9'
	'\D' : 'Any character thats NOT a numeric digit 0-9'
	'\w' : 'Any letter, normal digit or the underscore' # Think of me as matching WORD characters.
	'\W' : 'Anything thats not a letter, normal digit, or underscore'
	'\s' : 'Any space, tab, or newline character' # Think of me as matching "WHITESPACE characters"
	'\S' : 'Any character thats NOT a space, tab, or newline character'
	'()?' : 'I can match however many times I want. Or none at all'
	'()*' : 'I can match ANY amount of times my letters appear' # Bat(wo)?man == Batwowowowowoman
	'()+' : 'MUST match more than one time'
}