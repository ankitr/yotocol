#!/usr/bin/env python

import yo

def send_bit(bit, recipient, senders):
	if bit == None:
		return False
	sender = senders[int(bit)]
	sender.yo(recipient)
	def response():
		pass