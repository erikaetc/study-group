#the program parses users linked in profile and lists all the skills
from bs4 import BeautifulSoup
import urllib2
import sys
import sre

def parseAddress(input):
	if input[:7] != "http://":
		if input.find("://") != -1:
			print "Error: Cannot retrieve URL, address must be HTTP"
			sys.exit(1)
		else:
			input = "http://" + input
	return input

def retrieveWebPage(address):
	try:
		website = urllib2.urlopen(address)
	except urllib2.HTTPError, e:
		print "Cannot retrieve URL: HTTP Error code", e.code
		sys.exit(1)
	except urllib2.URLError, e:
		print "Cannot retrieve URL: " + e.reason[1]
		sys.exit(1)
	except:
		print "Cannot retrieve URL: unknown error"
		sys.exit(1)
	return website


if len(sys.argv) < 2:
	print "Expected Argument: URL"
	sys.exit(1)

address = parseAddress(sys.argv[1])
website_handle = retrieveWebPage(address)
website_text = website_handle.read()

soup = BeautifulSoup(website_text)
for skill in soup.findAll('span', {'class':'miniprofile-container'}):
	print skill.contents[0].strip()
