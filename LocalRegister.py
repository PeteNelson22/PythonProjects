print('Welcome to KBRegister...Select what you want to do!')
number=0
names=[]
names2=[]
def add(inputed_name):
    names.append(inputed_name)
def view():
    for name in names:
        print(name)
def remov(item):
    names.remove(item)
def tranfer():
    names.extend(names2)

while True:
    print('\t')
    print('1.Add name')
    print('2.View name')
    print('3.Remove name')
    print('4.Transfer data')
    print('5.Exit')

    choice = input('Select an option:  ')
    print('\t')

    if choice == '1':
        input_name = input('Enter your name:  ')
        number += 1
        add(input_name)
    elif choice == '2':
        view()
    elif choice == '3':
        item = input("Enter the item you want to remove:  ")
        remov(item)
    elif choice == '4':
        tranfer()
    elif choice == '5':
        break
    else:
        print('Wrong input')
