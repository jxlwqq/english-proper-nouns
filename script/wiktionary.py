# /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

domain = 'https://en.wiktionary.org'
start_url = domain + '/w/index.php?title=Category:English_proper_nouns'


def get_dict(url):
    print url
    res = requests.get(url)
    tree = etree.HTML(res.text)
    nouns = tree.xpath('//div[@class="mw-category-group"]//a/text()')
    for i, noun in enumerate(nouns):
        print noun
        # Processing data here
    next_url = ''
    try:
        next_url = tree.xpath('//a[text()="next page"][1]/@href')[0]
    except Exception:
        print 'no next page'
    if next_url:
        get_dict(domain + next_url)


get_dict(start_url)
