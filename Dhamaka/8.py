def main():
    num = int(input("Enter the number for the table: "))
    for i in range(1, 11):
        print(f'{num} * {i} = ', i*num)


if __name__ == '__main__':
    print("Program to print the multiplication of the table...")
    main()