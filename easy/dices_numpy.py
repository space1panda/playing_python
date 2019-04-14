import numpy as np
import argparse

"""
	Elementary manipulations without classes. Usage of console designer and numpy library. 
	
"""


	
def roll(size, dice_num,times):
	roll = np.random.randint(1,size*dice_num, size=times)
	print(np.average(roll))


np.random.seed(np.random.randint(1,10))

parser = argparse.ArgumentParser(description='Playing dices')
parser.add_argument('-s','--size', type=int, default=6,
                    help='provide size of a dice')
parser.add_argument('-dn','--dice_num', type=int, default=2,
                    help='provide number of dices')
parser.add_argument('-t','--times', type=int, default=10, help='provide number of rolls')
inputs = parser.parse_args()

roll(inputs.size, inputs.dice_num, inputs.times)
		
