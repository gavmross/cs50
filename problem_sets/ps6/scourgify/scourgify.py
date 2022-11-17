
import sys
import csv

def main():
    check_args(sys.argv) 
    cleaning(sys.argv[1], sys.argv[2])

def check_args(arg):
    if len(arg) > 3:
        sys.exit('Too many arguments')
    elif len(arg) < 3:
        sys.exit('Too few arguments')
    try: 
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('File does not exist') 
   
def cleaning(csv1,csv2):
    csv1 = sys.argv[1]
    csv2 = sys.argv[2]
    students = []
    with open(csv1) as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            students.append({'name': row['name'], 'house': row['house']})
    with open(csv2, 'a') as file2:
            writer = csv.DictWriter(file2, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
    for student in students:
        student['name'] = student['name'].split(',')
        last = student['name'][0]
        first = student['name'][1]
        house = student['house']
        
        with open(csv2, 'a') as file2:
            writer = csv.DictWriter(file2, fieldnames=['first', 'last', 'house'])
            writer.writerow({'last': last, 'first': first, 'house': house})

        

if __name__ == '__main__':
    main()