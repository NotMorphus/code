def main():
    ls =[]
    num = int(input("Enter the number of elements "))
    for i in range(0, num):
        n = int(input("Enter the element "))
        ls.append(n)
    for i in range(0, len(ls)):
        if ls[i]%2 == 0:
            print("This is a even number ", ls[i])
 

if __name__ == "__main__":
    print("Program to print all the even numbers in the list...")
    main()