def main():

    return order()


def order():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    while True: 
        try:
            order_list = []
            while True:
                item = input('Item: ')
                order_list.append(item.lower().title())
        except EOFError:
            total = 0
            for i in order_list:
                try:
                    total += menu[i]
                except KeyError:
                    pass
            return print('\nTotal: $' + str(format(total, '.2f')))


main()