#!usr/bin/env python
import sys

def args() -> str:
    try:
        return open(sys.argv[1]).readlines()
    except:
        return "Incorrect file format. Please input a file"

def parseFasta(fasta: str) -> dict:
    titles = {}
    current = ''
    for line in fasta:
        if line[0] == '>':
            current = line[1:].rstrip()
            titles[current] = ''
        else:
            titles[current] += line.rstrip()
    return titles

def gcCalculator(fasta: dict) -> list:
    highest_gc = ['', 0]
    for keys, values in fasta.items():
        gc_count = 0
        for nucleotides in values:
            if nucleotides == 'C' or nucleotides == 'G':
                gc_count += 1
        percentage = gc_count / len(values) * 100
        if (percentage > highest_gc[1]):
            highest_gc = [keys, percentage]
    return highest_gc

def main() -> None:
    fasta = args()
    fasta_dict = parseFasta(fasta)
    highest_gc = gcCalculator(fasta_dict)
    print(highest_gc[0])
    print(highest_gc[1])

if __name__ == '__main__':
    main()
