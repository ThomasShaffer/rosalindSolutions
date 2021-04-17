#!usr/bin/env python
import sys
def args() -> str:
	try:
		return open(sys.argv[1]).read().rstrip()
	except:
		return "Incorrect argument type. Please provide a file"

def main() -> None:
	sequence = args()
	counts = {"A": 0, "G": 0, "C": 0, "T": 0}
	for nucleotides in sequence:
		counts[nucleotides] += 1
	print(counts["A"],counts["C"],counts["G"],counts["T"])

if __name__ == '__main__':
	main()
