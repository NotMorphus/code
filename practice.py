#!/usr/bin/python3

# Q1 WAP to print a set of numbers seperated by comma in a single line which are divisble by 
#   7 and are not a multiple of 5

# Q2 WAP to print a set of numbers which are even between 1000 and 3000 where each digit of the number
#    is even and they should be seperated with a comma

# Q3 WAP a program to calculate upper and lower case letters in a string

def main():


	print("Q3 :\n")
	text = "Hello"
	upperc = lowerc = 0
	for i in text:
		if (i.isupper()):
			upperc = upperc + 1
		else:
			lowerc = lowerc + 1
	print("Upper :", upperc)
	print("Lower :", lowerc)

	print("Q1 :\n")
	for i in range(2000, 3201):
		if i%7 == 0 and i%5 != 0:
			print(i, end=',') # Q1

	print("Q2 :\n")
	for i in range(1000,3001):
		if i%2 == 0:
			n = i
			count = 0
			while n > 1:
				q = n%10
				n = n//10
				if q%2 == 0:
					count = count + 1
					#print(count)
				else:
					count = 0
					break
				if count == 4:
					print(i, end=',')  # Q2

	# A much more easier way to solve the second problem
	# We convert it into string and perform string manipulation in it
	for i in range(1000,3001):
		text = str(i)
		if (int(text[0])%2 == 0 and int(text[1])%2 == 0 and int(text[2])%2 == 0 and int(text[3])%2 == 0):
			print(text, end=',')

if __name__ == '__main__':
	main()