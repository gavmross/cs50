def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return is_true(s) & char_num(s) & num_place(s) & syntax(s)
    

def is_true(s):
    if s[0:2].isnumeric():
        return False
    else:
        return True 
 
def char_num(s):
    if len(s) > 6 or len(s) < 2:
        return False
    else:
        return True
def num_place(s):
    if s[-1].isalpha():
        return False
    for i in range(len(s)):
        if s[i].isdigit() and s[:i].isalpha() and s[i] == '0':
            return False
        else: 
            tf = True
    return tf 
def syntax(s):
    return s.isalnum()

main()