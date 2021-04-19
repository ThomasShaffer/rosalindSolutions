#!usr/bin/env python
import sys

def args() -> [int,int]:
	try:
		return [int(sys.argv[1]), int(sys.argv[2])]
	except:
		return 'Incorrect input format. Please input two integers.'

def rabbit_fib(generation: int, litter: int, memory) -> int:
	if generation in memory:
		return memory[generation]
	if generation <= 2:
		return 1
	memory[generation] = rabbit_fib(generation-1,litter,memory) + (litter* rabbit_fib(generation-2,litter,memory))
	return memory[generation]
										

def main() -> None:
	arguments = args()
	generations = arguments[0]
	litter_size = arguments[1]
	memo = {}
	size = rabbit_fib(generations, litter_size, memo)
	print(size)

if __name__ == '__main__':
	main()


