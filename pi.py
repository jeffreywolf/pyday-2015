#! /usr/bin/env python

import argparse
import numpy as np

def getArgs():
	parser = argparse.ArgumentParser(
		description = "Simulate Pi"
	)
	parser.add_argument(
		"-n",
		type = int,
		required = True,
		help = "Number of random points to draw"
	)
	return parser.parse_args()

def dist(x,y):
	z = np.sqrt((x)**2+(y)**2)
	return z

def count_circle_pts(z):
	pz = z<1.0
	return sum(pz)

def simulate_pi(n):
	# square is 2 x 2
	x = np.random.uniform(-1,1,n)
	y = np.random.uniform(-1,1,n)
	z = dist(x,y)
	circle_pts = count_circle_pts(z)
	return circle_pts/float(n)*4

def main():
	args = getArgs()
	result = simulate_pi(args.n)
	print result

if __name__ == "__main__":
	main()