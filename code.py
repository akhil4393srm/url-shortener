from pyshorteners import Shortener 
ACCESS_TOKEN = 'YOUR TOKEN'
long_url = input()
url_shortener = Shortener('Bitly', bitly_token = ACCESS_TOKEN) 
print ("Short URL is {}".format(url_shortener.short(long_url)))
short_url = input()
url_expander = Shortener('Bitly', bitly_token = ACCESS_TOKEN)
print ("Long URL is {}".format(url_expander.expand(short_url)))
