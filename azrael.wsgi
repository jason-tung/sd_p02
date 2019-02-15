#!/usr/bin/python3

import sys

import logging

logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,'/var/www/azrael/')



from azrael import app as application 

