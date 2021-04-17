#!/usr/bin/env python
import sys

def args() -> str:
    try:
        return open(sys.argv[1]).read().rstrip()
    except:
        return 'Incorrect argument type given, please input a file'

def main():
	dna_sequence = args()
	rna_sequence = dna_sequence.replace('T', 'U')
	print(rna_sequence)
if __name__ == '__main__':
	main()
