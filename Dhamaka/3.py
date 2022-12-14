def main():
    sum = 0
    ls = []
    num = int(input("Enter the number of elements "))
    for n in range(0, num):
        n = int(input("Enter element "))
        ls.append(n)
    for i in range(0, len(ls)):
        sum = sum + ls[i]
    print(sum, "is the sum of the list elements")


if __name__ == '__main__':
    print("Program to add the elements in the list...")
    main()