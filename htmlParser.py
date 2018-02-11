'''
plan :
read the html content from url
decipher the required text
populate a variable with the values as json
populate a variable with values as csv
save to file
'''
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

response = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions')
html = response.read()

print(html)

#doesnt work
