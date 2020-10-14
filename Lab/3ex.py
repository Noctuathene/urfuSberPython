
def search_char(inp_str, inp_char):
    f = 0
    for i in range(len(inp_str)):
        if inp_char == inp_str[i]:
            f +=1
            if f==2:
                return i
    return -1

print(search_char("asdfasdf","f"))            
