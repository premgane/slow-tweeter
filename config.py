#!/bin/env/python

import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'csrf-protection'

	TWITTER_CONSUMER_KEY = os.environ.get('CONSUMER_KEY') or 'a'
	TWITTER_CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET') or 'b'
	TWITTER_ACCESS_KEY = os.environ.get('ACCESS_KEY') or 'c'
	TWITTER_ACCESS_SECRET = os.environ.get('ACCESS_SECRET') or 'd'

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'e'
	SQLALCHEMY_TRACK_MODIFICATIONS = False