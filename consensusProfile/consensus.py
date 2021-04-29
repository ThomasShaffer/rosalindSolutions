#! /usr/bin/env python
import sys

def args() -> str:
	try:
		return open(sys.argv[1]).readlines()
	except:
		return 'Incorrect input format. Please input a file'

def parse_fasta(fasta_files: list) -> list:
	i = -1
	sequences = []
	for line in fasta_files:
		if line[0] == '>':
			i += 1
			sequences.append('')
			continue

		else:
			sequences[i] += line.rstrip()

	return sequences

def find_consensus(sequences: list) -> str:
	

def main() -> None:
	fasta_sequences = args()
	sequences = parse_fasta(fasta_sequences)
	#consensus, profile_matrix = find_consensus(sequences)


if __name__ == '__main__':
	main()

