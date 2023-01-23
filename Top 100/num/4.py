#!/usr/bin/python3

def bin2dec(n):
    basev = 1
    sum = 0
    print(n)
    while n > 0:
        r = n%10
        sum = sum + basev * r
        n = n//10
        basev = basev * 2
    print(sum)

def main():
    pass
    num = int(input("Enter the binary number :"))
    bin2dec(num)

if __name__ == '__main__':
    main()
