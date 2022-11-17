import tabulate
import sys
import csv

def main():
    check_args(sys.argv) 
    pizza(sys.argv[1])

def check_args(arg):
    if len(arg) > 2:
        sys.exit('Too many arguments')
    elif len(arg) < 2:
        sys.exit('Too few arguments')
    try: 
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('File does not exist') 
   

def pizza(file):
    pizzas = []
    with open(file) as file:
        reader = csv.reader(file) # UNDERSTAND READER MORE 
        for type, small, large in reader:
            pizzas.append({'Sicilian Pizza': type, 'Small': small, 'Large': large})
    print(tabulate.tabulate(pizzas[1:], headers='keys', tablefmt='grid')) 
        

if __name__ == '__main__':
    main()