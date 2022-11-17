def main():
    convert(fraction)
    guage(percentage)

def convert(fraction):
    while True: 
        try:
            usr_nums = input('Fraction: ').split('/')
            if usr_nums[0] > usr_nums[1]: usr_nums[1] = 0
            fraction = (int(usr_nums[0]) / int(usr_nums[1])) * 100
        except (ValueError, ZeroDivisionError):
            print('Input must be an integer, the denominator must be greater than 0, and the numerator must be less than denominator.')
        else:
            break
def guage(percentage):
    fuel_gauge = str(round(percentage)) + '%'
    if percentage <= 1: return 'E'
    elif percentage >= 99: return 'F'
    else: return fuel_gauge

if __name__ == '__main__':  
    main()