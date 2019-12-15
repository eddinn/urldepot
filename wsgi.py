#!/usr/bin/python3
import os
import sys
import logging
from spjald import app as application


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/fegurdspa/html/spjald")
