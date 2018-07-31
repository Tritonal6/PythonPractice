import json
import os
import random
import requests
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# Insert your target url below. Ensure that it's the proper URL that the
## form data is ACTUALLY being sent to.
url = input('')

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@urascrub.com'
    password = ''.join(random.choice(chars) for i in range(6))
# Input for both username and password should be the form data that you see when
## inspecting the network headers for the form submission. This is typically
### encoded - use the encoded array of characters.
    requests.post(url, allow_redirects=False, data={
        'InsertEncodedUsernameField': username, # encoded username field
        'InsertEncodedPasswordField': password # encoded password field
    })
