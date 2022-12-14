def calcrev(n):
    ls = []
    while n > 0:
        rem = str(int(n % 10))
        n = n // 10
        ls.append(rem)
    fin = ''.join(ls)
    return fin

def main():
    num = int(input("Enter the number :"))
    res = calcrev(num)
    if res == str(num):
        print("Palindrome")
    else:
        print("Not palindrome")
    
if __name__ == '__main__':
    main()