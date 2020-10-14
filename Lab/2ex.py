arr = input("введите числа через пробел Arr:").split()
n = int(input("число N:"))

def sqr_n(arr, n):
    if len(arr) >= n and not n<0:
        print(arr)
        return int(arr[n-1])**n
    else:
        return -1

print(sqr_n(arr, n))
    
