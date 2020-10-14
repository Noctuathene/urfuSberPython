x = input().split()
try:
    print("1й:{}; 3й:{}; 2й с конца:{}".format(x[0],x[2],[-2]))
except IndexError:
    print("Размер массива меньше 2")
