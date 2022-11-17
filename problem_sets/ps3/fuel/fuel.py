def main():
    print(fuel())

def fuel():
    while True: 
        try:
            usr_nums = input('Fraction: ').split('/')
            if usr_nums[0] > usr_nums[1]: usr_nums[1] = 0
            fraction = (int(usr_nums[0]) / int(usr_nums[1])) * 100
        except (ValueError, ZeroDivisionError):
            print('Input must be an integer, the denominator must be greater than 0, and the numerator must be less than denominator.')
        else:
            break
    fuel_gauge = str(round(fraction)) + '%'
    if fraction <= 1: return 'E'
    elif fraction >= 99: return 'F'
    else: return fuel_gauge

main()