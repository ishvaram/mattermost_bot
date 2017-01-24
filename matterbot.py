'''
!/usr/bin/python3
-*- coding: utf-8 -*-
Author: Kovalan R
Date: 24-01-2017
Description: Mattermost bot respond_to from Exotel 
MySQL data source and does the given operations
'''
from time import sleep
from mattermost_bot.bot import Bot 
from mattermost_bot.bot import respond_to
import re
import collections
import os, sys

import MySQLdb
db = MySQLdb.connect(host="",    # your host, usually localhost
                     user="",         # your username
                     passwd="",  # your password
                     db="") 

cur = db.cursor()


#to get the query result
def get_query_result(query,my_cur):
	try:
	    my_cur.execute(query)
	    desc = my_cur.description
	    result = [dict(zip([col[0] for col in desc], row)) for row in my_cur.fetchall()]
	    return result
	except Exception,e:
		raise e
		

@respond_to('ref id (.*)')
def give_me(message, something):
	# Use all the SQL you like
	query  = "SELECT * FROM AvailablePhoneNumber where AccountSid = '{0}' limit 3".format('')
	datum = get_query_result(query,cur)
	print datum
	message.reply('Result Set for Sid %s' % datum)


if __name__ == "__main__":
	print ('socket started')
	Bot().run()

    # sleep(10)
