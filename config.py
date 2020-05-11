#!/bin/env/python

import os

class Config(object):
	CONSUMER_KEY = os.environ.get('CONSUMER_KEY') or 'you-will-never-guess'
	CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET') or 'you-will-never-guess'
	ACCESS_KEY = os.environ.get('ACCESS_KEY') or 'you-will-never-guess'
	ACCESS_SECRET = os.environ.get('ACCESS_SECRET') or 'you-will-never-guess'