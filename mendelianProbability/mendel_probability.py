#! usr/bin/env python

import sys

def args():
	try:
		return [i for sys.argv[i] in range(1,4)]
	except:
		return 'Incorrect input format. Please input 3 separate integers'

def dominant_probability(numbers: list) -> float:
	#numbers of populations
	#AA -> homozygous dominant
	#Aa -> heterozygous
	#aa -> homozyogus recessive

	AA = numbers[0]
	Aa = numbers[1]
	aa = numbers[2]


def main() -> None:
	population = args()
	probability = dominant_probability(args)
	print(probability)

if __name__ == '__main__':
	main()
