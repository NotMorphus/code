def main():
    ls = list(input("Enter the list to check "))
    print("The list entered is ", ls)
    print("The unique elements are", list(set(ls)))


if __name__ == '__main__':
    print("Program to print unique elements in the list...")
    main()