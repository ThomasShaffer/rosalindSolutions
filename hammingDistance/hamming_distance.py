#!usr/bin/env python
import sys

def args() -> list:
	try:
		return open(sys.argv[1]).readlines()
	except:
		return "Incorrect format file. Please input a text file"

def hamming_distance(sequence1: str, sequence2: str) -> int:
	distance = 0
	for index in range(len(sequence1)):
		if sequence1[index] != sequence2[index]:
			distance += 1
	return distance


def main() -> None:
	sequences = args()
	sequence_one = sequences[0]
	sequence_two = sequences[1]
	distance = hamming_distance(sequence_one,sequence_two)
	print(distance)




if __name__ == '__main__':
	main()
