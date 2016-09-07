# import urllib3
#
# site = 'http://bitbucket.org/tortoisehg/stable/wiki/Home/ReleaseNotes'
# req = urllib3.HTTPResponse(site)
# text = req.read()
# print(text)

import urllib.request
fhand=urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
print(fhand.read())