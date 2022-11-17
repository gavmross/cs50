import sys

def main():
    check_args(sys.argv)
    print(count_lines(sys.argv[1]))

def check_args(arg):
    if len(arg) > 2:
        sys.exit('Too many arguments')
    elif len(arg) < 2:
        sys.exit('Too few arguments')

def count_lines(file):
    count = 0
    try:
        with open(file) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit('File does not exist')
    for line in lines:
        if len(line.lstrip()) > 0:
            count +=1
        else: continue 
    return count
 
if __name__ == '__main__':
    main()