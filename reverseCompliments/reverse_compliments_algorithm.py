import sys

def args():
	try:
		return open(sys.argv[1]).read().rstrip()
	except:
		return 'Incorrect input format. Please input a file'

def compliments(sequence) -> str:
	compliments = {'A': 'T', 'T':'A','G':'C','C':'G'}
	compliment_sequence = ''
	for nucleotide in sequence:
	    	compliment_sequence += compliments[nucleotide]
	return compliment_sequence

def reverse(string):
    length = len(string)
    list_string = list(string)
    left_pointer = 0
    right_pointer = length - 1
    while left_pointer != (length // 2):
        temp = list_string[left_pointer]
        list_string[left_pointer] = list_string[right_pointer]
        list_string[right_pointer] = temp
        left_pointer +=1
        right_pointer -= 1
    return ''.join(list_string)

def main():
	sequence = args()
	reverse_compliments = reverse(compliments(sequence))
	print(reverse_compliments)


if __name__ == '__main__':
	main()
