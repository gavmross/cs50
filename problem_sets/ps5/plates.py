def main():
    plate = input("Plate: ")
    print(is_valid(plate))

def is_valid(s):
    if is_true(s) and char_num(s) and num_place(s) and syntax(s):
        return "Valid"
    else: 
        return 'Invalid'

    

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

if __name__ == '__main__':
    main()