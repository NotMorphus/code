#!/usr/bin/python3

#Regex program to find out the Mobile Numbers starting with +91
def main():
    count = int(input("Enter how many numbers you want to enter :"))
    for i in range(count):
        pattern = '^\+91[0-9]{10}'
        number = input("Enter the number you want :")
        res = re.search(pattern, number)
        if res:
            print(res.group())
        else:
            print("No. does not match the pattern")

if __name__ == '__main__':
    main()
