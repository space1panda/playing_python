from random import choice
from statistics import mean
import argparse

"""
	Elementary manipulations without classes. Usage of console designer. 
	
"""


def dice(size):
	return choice(list(range(1,size)))
	
def roll(size,times):
	results = []
	i=0
	while i < times:
		results.append(dice(size)+dice(size))
		i+=1
	print(int(mean(results)))



parser = argparse.ArgumentParser(description='Playing dices')
parser.add_argument('-d','--dice', type=int, default=6,
                    help='provide size of a dice')
parser.add_argument('-t','--times', type=int, default=10, help='provide number of rolls')
inputs = parser.parse_args()

roll(inputs.dice, inputs.times)
		
