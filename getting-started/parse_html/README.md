HTML parsing tool
================================

Parses html using provided url link, returns all elements which contain
specified tag_name, key and value. Also possible limit output by number of records.
Default limit is 5.

Dependencies
-------------------------
HTML parsing tool have dependencies to lxml and BeautifulSoup4 libraries
so you need to install them in order to use the tool

        sudo pip install lxml beautifulsoup4

 or

        virtualenv env
        source env/bin/activate
        pip install lxml beautifulsoup4

Usage example
-------------------------

Get 10 last attendess from PyLadies meetup

        parse_html.py --url http://www.meetup.com/PyLadiesStockholm/events/122636662/ \
        --tag_name h5 --key class --value 'padding-none member-name' --limit 10