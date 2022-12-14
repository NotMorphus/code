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
    print("The reverse of the digits is :", res)
    
if __name__ == '__main__':
    main()