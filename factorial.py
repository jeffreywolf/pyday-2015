#! /usr/bin/env python

import argparse

def getArgs():
	parser = argparse.ArgumentParser(
		description = """Factorial calculator
		"""
	)
	parser.add_argument(
		"-n",
		type = int,
		required = True,
		help = "Enter n to set N!"
	)

	return parser.parse_args()

def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)

def main():
	args = getArgs()
	result = factorial(args.n)
	print result

if __name__ == "__main__":
	main()