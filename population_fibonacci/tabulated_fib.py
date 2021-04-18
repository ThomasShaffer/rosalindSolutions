#!usr/bin/env python
import sys

def args() -> [int,int]:
	try:
		return [int(sys.argv[1]),int(sys.argv[2])]
	except:
		return 'Incorrect input format. Please input two integers.'

def fibonacci(generations: int, litter_size: int) -> int:
	array = [0,1,1]
	if generations <= 2:
		return 1
	for index in range(2,generations):
		array.append(array[index] + (array[index - 1] * litter_size))
	return max(array)


def main() -> None:
	generations, litter_size = args()
	population_size = fibonacci(generations, litter_size)
	print(population_size)



if __name__ == '__main__':
	main()
