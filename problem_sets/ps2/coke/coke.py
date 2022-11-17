def coke():
    due = 50
    while  0 < due <= 50:
        cents = int(input('Insert Coin: '))
        due = due - cents
        if due < 0:
            return print('Change owed: ', abs(due))

        print('Amount due: ', due)
        
    

coke()