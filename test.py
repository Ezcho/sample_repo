#피보나치 수의 나열
#n번째 fibo는 뭐냐?

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(6))