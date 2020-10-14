string = input("передай пароль: ")
def check_pass(string):
    if len(string)>16 and string.isalnum() :
        upChar, lowChar, numChar= False,False,False
        for i in string:
            if i.islower():
                upChar = True
            if i.isupper():
                lowChar = True
            if i.isdigit():
                numChar = True
        return upChar and lowChar and numChar
    else:
        return False
print(bool(check_pass(string)))
