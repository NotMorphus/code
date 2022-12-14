def main():
    ls =[]
    num = int(input("Enter the number of elements "))
    for i in range(0, num):
        n = int(input("Enter the element "))
        ls.append(n)
    print("The maximum element is ",max(ls))
    print("The minimum element is ", min(ls))


if __name__ == '__main__':
    print("Program to print max and min of a list of numbers...")
    main()