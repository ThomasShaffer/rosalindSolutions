#! /usr/bin/env python
import sys

def args() -> list:
	try:
		return open(sys.argv[1]).readlines()
	except:
		return 'Please input the correct format, which is a file'

def find_motif(main_string: str, substring: str) -> [int]:
	occurences = []
	print(main_string, substring)
	for index in range(len(main_string)):
		if main_string[index:index+len(substring)] == substring:
			occurences.append(index+1)
	return occurences



def main():
	main_string, sub_string = args()
	occurences = find_motif(main_string.rstrip(), sub_string.rstrip())
	for index in occurences:
		print(index, end = ' ')





if __name__ == '__main__':
	main()
