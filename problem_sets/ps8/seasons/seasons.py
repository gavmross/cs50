import sys 
from datetime import date
import inflect 

def main():
    bday = input('Date of Birth: ')
    print(birthday(bday))



def birthday(bday):
        
        try:
            input_bday_date = bday.split('-')
            year = int(input_bday_date[0])
            month = int(input_bday_date[1])
            day = int(input_bday_date[2])
            return_date = date(year, month, day)
            total_days = date.today() - return_date 
            total_mins = total_days * 1440
            p = inflect.engine()
            in_mins = p.number_to_words(total_mins).replace(',','').replace('and', '')
            return in_mins + ' minutes'
        except ValueError:
            return 'Wrong format'

if __name__ == "__main__":
    main()