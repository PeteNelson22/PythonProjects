print('Welcome to Admin Dashboard')
out = []
def addpayroll():
    info = {}
    info['Name:'] = input('Enter Name: ')
    info['Position:'] = input('Enter Position: ')
    info['Entry Year:'] = input('Enter Entry Year: ')
    info['Salary:'] = input('Enter Salary: ')
    out.append(info)

def view():
    for details in range(len(out)):
        detail=out[details]
        print(detail['Name:'],'\n',detail['Position:'],'\n',detail['Entry Year:'],'\n',detail['Salary:'])

def removedetails(x):
    del out[item]

#def deleteall():

name=input('Enter Name: ')
password=input('Enter Password: ')

if (name=="admin" or name=='nelson') and password=='12345':
    print(f'Welcome {name}!')
    while True:
        print('1. Add info: ')
        print('2. View all: ')
        print('3. Remove info: ')
        print('4. Delete all info: ')
        print('5. Logout: ')

        choice = input('Enter Your Option: ')
        if choice == '1':
            addpayroll()
        elif choice == '2':
            view()
        elif choice == '3':
            item = int(input('Enter the index of the info: '))
            removedetails(item) #remove item base on it index
        #elif choice == '4':
            #deleteall()
        elif choice == '5':
            break

else:
   print('Sorry! you are not an admin')



