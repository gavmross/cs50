from multiprocessing.sharedctypes import Value


def main():
    return date()

def date():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True: 
        input_date = input('Date: ')
        if '/' in input_date:
            date_list = input_date.split('/')
        else: 
            date_list = input_date.replace(',','')
            date_list = date_list.split()
        try:
            month, day, year = int(date_list[0]), int(date_list[1]), int(date_list[2])
        except ValueError:
            month, day, year = date_list[0], int(date_list[1]), int(date_list[2])
            for i in months:
                if month == i: month = months.index(i) + 1
        if month > 12 or day > 31: 
            pass
        else: 
            break


    if month < 10 and day < 10:
        print(str(year)+'-'+str(f'{month:02}')+'-'+str(f'{day:02}'))
    elif day < 10:
        print(str(year)+'-'+str(month)+'-'+str(f'{day:02}'))
    elif month < 10:
        print(str(year)+'-'+str(f'{month:02}')+'-'+str(day))
    else: 
        print(str(year)+'-'+str(month)+'-'+str(day))
    
main()