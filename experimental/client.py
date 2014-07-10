#!/usr/bin/env python

import yo
import time
import threading
import sys

def run(config=None):
	print('Preparing Yotocol client.')

	YO_LATENCY_FIVE_SIGMA = 3.0
	# seconds
	YO_MAX_SPIKE_HEIGHT = 1024
	# max yos sent per spike
	THE_STUFF = 'abcdefghijklmnopqrstuvwxyz ,.!?\''


	globals()['YO_RECEIVED_STATE'] = 0
	# number of yos over past YO_LATENCY_FIVE_SIGMA

	def monitor_received_state():
	  time.sleep(YO_LATENCY_FIVE_SIGMA/2)
	  time_start = time.time()
	  loop_number = 0
	  while True:
	    time.sleep(time_start + YO_LATENCY_FIVE_SIGMA * loop_number - time.time())
	    threading.Thread(target = new_sequence, args = (globals()['YO_RECEIVED_STATE'],)).start()
	    globals()['YO_RECEIVED_STATE'] = 0
	    loop_number += 1

	def receive_callback():
	  globals()['YO_RECEIVED_STATE']+=1

	def new_sequence(size):
	  five_bit_one = size&((1<<6)-1)
	  five_bit_two = (size - five_bit_one)//(2**5)
	  sys.stdout.write(THE_STUFF[five_bit_one]+THE_STUFF[five_bit_two])

	threading.Thread(target = monitor_received_state)
	yo.sup(USERNAME, receive_callback)