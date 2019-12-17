#!/usr/bin/python3
import os
import sys
import logging
from urldepot import app as application


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/urldepot")
