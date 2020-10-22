def addtolist(file, item):
    file.write(item + '\n')

def delete(file, item_number):
    file.seek(0)
    items = list(enumerate(file.read().split(), 1))
    del items[item_number -1]
    with open('list.txt', 'w') as file:
        for item in items:
            file.write(item[1] + '\n')

def viewlist(file):
    file.seek(0)
    # Enumerate List
    items = list(enumerate(file.read().split(),1))
    for count, item in items:
        print(str(count) + ') ' + item)

def main():
    print('---Shopping List---')
    print('Commands:\n !quit - to quit\n !list - to view list\n !delete - to delete an item')
    while True:
        with open('list.txt', 'a+') as file:
            item = input('Enter an item: ')
            if item == '!quit':
                break
            elif item == '!list':
                viewlist(file)
            elif item == '!delete':
                itemtd = int(input('Delete which item number: '))
                delete(file, itemtd)
                viewlist(file)
            else:
                addtolist(file, item)


if __name__ == '__main__':
    main()
