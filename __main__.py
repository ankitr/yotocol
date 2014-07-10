#!/usr/bin/env python

import traceback

from argparse import ArgumentParser

import client
import server
import yo


def new_name(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def register_name(name):
	try:
		yo.make(name)
	except NameError:
		register(new_name)

parser = ArgumentParser(
    description='Transfer data over the YDTP (Yo Data Transfer Protocol), or Yotocol for short.')

parser.add_argument('-l', '--burst-latency', nargs=1,
                    help='The period between bursts.', type=int, default=3000)
parser.add_argument('-s', '--burst-size', nargs=1,
                    help='The height of your bursts.', type=int, default=1024)
parser.add_argument('-u', '--users', nargs=2, help='The user names you would like to use.',
                    default=[new_name(), new_name()])
parser.add_argument(
    'command', nargs=1, help='The process you would like to run.')
parser.add_argument(
	'-c', '--content', nargs=1, help='The ASCII content of the message you would like to send.')

args = parser.parse_args()

commands = {
    'client': client,
    'server': server
}

users = []

for name in args.users:
	users.append(register_name(name))

try:
    commands[args.command].run(args.burst_latency, args.burst_size, users.)
except KeyError:
    print('Invalid command type.')
except StandardError as e:
    print('Unknown error. Printing traceback.')
    print(traceback.format_exec())