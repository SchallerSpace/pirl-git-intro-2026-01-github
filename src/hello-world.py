#!/usr/bin/env python3

import random

worlds = [ "Earth", "Moon", "Mars", "Europa", "Pluto" ]
weights = [ 10, 2, 20, 5, 1 ]

def main():

	for i in range(10):
		greet()

def greet():

	print(f"Hello, {random.choices(worlds, weights=weights)[0]}!")

if __name__ == '__main__':
	main()
