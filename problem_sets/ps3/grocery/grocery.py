def main():
    return grocery()

def grocery():
        groceries = []
        try:
            while True:
                item = input()
                groceries.append(item.lower())
        except EOFError:
            pass
        count = []
        groceries_no_duplicate = []
        [groceries_no_duplicate.append(i) for i in groceries if i not in groceries_no_duplicate]
        for grocery in groceries_no_duplicate:
            count.append(groceries.count(grocery))
        
        for i in range(len(count)):
            print(count[i], groceries_no_duplicate[i].upper())

main()