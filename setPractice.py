names = set([])

def addname(x):
    names.add(inputed_name)

def addnames(x):
    names.update(inputed_name)

def view():
    for name in names:
        print(str(name))

def remove(x):
    names.remove(inputed_name)

while True:
    print('1. Add a single name: ')
    print('2. Add multiple name: ')
    print('3. View names')
    print('4. Remove names')

    choice = input('Enter your choice: ')

    if choice=='1':
        inputed_name = input('Enter your name: ')
        addname(inputed_name)
    elif choice=='2':
        inputed_name = input('Enter multiple names: ')
        addnames(inputed_name)
    elif choice=='3':
        view()
    elif choice=='4':
        inputed_name = input('Enter name: ')
        remove(inputed_name)
    else:
        break


