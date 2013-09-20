#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup
import argparse
import sys

def read_html(url):
    '''
    Function gets html document from url address
    '''
    try:
        request = urllib2.urlopen(url)
        html_doc = request.read()
        request.close()
        return (True, BeautifulSoup(html_doc))
    except urllib2.URLError as e:
        return (False, str(e)) 

def replace_ascii(str):
    '''
    Function replaces swedish characters for sensible duplicates
    '''
    str = str.replace(u'\xc5','A')
    str = str.replace(u'\xe5','a')
    str = str.replace(u'\xc4','A')
    str = str.replace(u'\xe4','a')
    str = str.replace(u'\xd6','O')
    str = str.replace(u'\xf6','o') 
    return str.encode('ascii','replace')

def parse_html(soup, tag_name, key, value):
    '''
    Function parses html document and returns list of matches
    '''
    matches = []
    for tag in soup.findAll(tag_name, attrs = {key : value}):
        for line in tag.stripped_strings:
            matches.append(replace_ascii(line))
    return matches
    
if __name__ == "__main__":
    # Define user interface options
    parser = argparse.ArgumentParser(description='Parses html using provided url'
                                     ' link, returns all elements which contain '
                                     'specified tag_name, key and value.')
    parser.add_argument('--url', type=str, required=True, help='a string, '
                        'web page')
    parser.add_argument('--tag_name', type=str, required=True, help='a string, '
                        'name of an element')
    parser.add_argument('--key', type=str, required=True, help='a string, an '
                        'attribute of the specified element, by default = class')
    parser.add_argument('--value', type=str, required=True, help='a string, '
                        'an attribute of the specified element')
    parser.add_argument('--limit', type=str, default=5, help='number '
                        'of records to show')
    args = parser.parse_args()

    # Get page content
    (status, output) = read_html(args.url)
    if status != True:
        print "Can't parse provided url! %s" % output
        sys.exit(1)

    # Get elements that match provided parameters
    elements = parse_html(output, args.tag_name, args.key, args.value)
    if not elements:
        print "Nothing found for your request"
        sys.exit(0)

    # Cut list of elements if it is longer than defined limit
    if len(elements) <= int(args.limit):
        pass
    else:
        elements = elements[-int(args.limit):]

    # Print results
    print "The following were found:"
    for elem in elements:
        print elem





