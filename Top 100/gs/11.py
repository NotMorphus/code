def calcsum(n):
    fin = 0
    while n > 0:
        rem = int(n % 10)
        n = n // 10
        fin = fin + rem
    return fin

def main():
    num = int(input("Enter the number :"))
    res = calcsum(num)
    print("The sum of the digits is :", res)
    
if __name__ == '__main__':
    main()