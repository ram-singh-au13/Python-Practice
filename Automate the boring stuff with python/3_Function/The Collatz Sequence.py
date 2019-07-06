def collatz(n):
    if n == 1:
        return
    if n%2 == 0 :
        print(n // 2)
        return collatz(n // 2)
    else :
        print(n*3 + 1)
        return collatz(n*3 + 1)

if __name__ == '__main__':

    while True :
        n = int(input('Enter the positive number : '))
        if n<=0 :
            print('!! Number should be greater than 0 !!')
        else : break
    
    print('-- Collatz sequence -- : ')
    collatz(n)
        
