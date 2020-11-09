# Imports http requests module
import requests

# Imports emoji module
import emoji

# Makes a request to a website
r = requests.get("https://www.bbc.co.uk")

# If the website is running (code = 200)
if r.status_code == 200:
    # Emojize is emoji module's way of turning text into an emoji
    print(emoji.emojize("Website is Live! :thumbs_up:"))
# In any other case
else:
    print(emoji.emojize("Website is dead... :thumbs_down:"))
