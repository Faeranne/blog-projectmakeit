#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://projectmakeit.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATAGORY_FEED_RSS = 'feeds/%s.rss'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "projectmakeit"
GOOGLE_ANALYTICS = 'UA-30850899-1'
