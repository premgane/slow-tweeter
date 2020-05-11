#!/bin/env/python

import os

class Config(object):
	TWITTER_CONSUMER_KEY = os.environ.get('CONSUMER_KEY') or 'you-will-never-guess'
	TWITTER_CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET') or 'you-will-never-guess'
	TWITTER_ACCESS_KEY = os.environ.get('ACCESS_KEY') or 'you-will-never-guess'
	TWITTER_ACCESS_SECRET = os.environ.get('ACCESS_SECRET') or 'you-will-never-guess'

	DATABASE_URL = os.environ.get('DATABASE_URL') or 'you-will-never-guess'