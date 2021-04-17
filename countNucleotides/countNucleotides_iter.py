#!/usr/bin/env python
import sys

def args() -> str:
    try:
        return open(sys.argv[1]).read().rstrip()
    except:
        return 'Incorrect argument type given, please input a file'


def main() -> None:
    """ Make a jazz noise here """
    sequence = args()
    A, G, C, T = 0, 0, 0, 0
    for nucleotide in sequence:
        if nucleotide == 'A':
            A += 1
        elif nucleotide == 'G':
            G += 1
        elif nucleotide == 'C':
            C += 1
        elif nucleotide == 'T':
            T += 1
    print(A, G, T, C)
        

# --------------------------------------------------
if __name__ == '__main__':
    main()