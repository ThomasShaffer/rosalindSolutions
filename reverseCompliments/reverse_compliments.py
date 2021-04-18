#!usr/bin/env python
import sys

def args() -> str:
	try:
		return open(sys.argv[1]).read().rstrip()
	except:
		return 'Incorrect input format. Please insert a file'

def compliment(sequence) -> str:
	compliments = {'A': 'T', 'T':'A','G':'C','C':'G'}
	compliment_sequence = ''
	for nucleotide in sequence:
		compliment_sequence += compliments[nucleotide]
	return compliment_sequence

def main() -> None:
	sequence = args()
	forward_compliment = compliment(sequence)
	print(forward_compliment[::-1])


if __name__ == '__main__':
	main()
