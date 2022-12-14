def main():
    ls1 = list(input("Enter the list1:"))
    ls2 = list(input("Enter the list2:"))
    ls3 = ls1[:]
    for i in ls3:
        if i in ls2:
            ls1.remove(i)
            ls2.remove(i)
    print("List 1 :", ls1)
    print("List 2 :", ls2)

if __name__ == '__main__':
    print("Program to remove common elements from 2 lists...")
    main()