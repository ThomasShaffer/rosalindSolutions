#! /usr/bin/env python
import sys

def args() -> str:
	try:
		return open(sys.argv[1]).read().rstrip()
	except:
		return 'Incorrect input format. Please include a file to read'

def translation(rna: str) -> str:
	map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
	protein = ''
	for i in range(0, len(rna), 3):
		codon = rna[i:i+3]
		amino_acid = map[codon]
		if amino_acid != 'STOP':
			protein += map[codon]
		else:
			return protein
	return protein




def main() -> str:
	rna_sequence = args()
	protein_strand = translation(rna_sequence)
	print(protein_strand)


if __name__ == '__main__':
	main()
