def main():
    num = int(input("Enter the number :"))
    count = 0
    while num > 0:
        num = int(num/10) 
        count = count + 1
    print("The digit count is ", count)

if __name__ == '__main__':
    print("Program to count the totla number of digits in a number...")
    main()