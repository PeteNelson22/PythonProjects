class Student:

    def __init__(self,id,name,fees):
        self.id = id
        self.name = name
        self.fees = fees

    def display(self):
        print(self.id, self.name, self.fees)

while True:
    print('1.Enter Info')
    print('2.Display')
    print('3.Display a particular info')
    option = input('Choose: ')
    if option == '1':
        id = input('ENTER ID: ')
        name = input('ENTER NAME: ')
        fees = input('ENTER FEES: ')
        student = Student(id,name,fees)
    if option == '2':
        student.display()
        break
    # if option == '3':
    #     query = input('Enter: ')
    #     print(getattr(student,query))


    # student.display()
    # enquiry = input('Do you want to continue? Type y or n ')
    # if enquiry == 'N' or 'n':
    #     break
