num_str = "30000"
def search_zero(num_str):
    f=0
    for i in range(len(num_str)):
        if int(num_str[-(i+1)]) == 0:
            f+=1
        else:
            return f
print(search_zero(num_str))
