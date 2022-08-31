import mysql.connector
from datetime import datetime



class NelsonPay:

    def addNames(self):
        sql = """INSERT INTO payroll(id,first_name,last_name,company_id,position,salary,register_date)
              VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        id = input('ID: ')
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        company_id = input('Company Id: ')
        position = input('Position: ')
        salary = input('Salary: ')
        register_date = date
        val = (id, first_name, last_name, company_id, position, salary, register_date)

        try:
            cursor.execute(sql, val)
            con.commit()
            print(f'Successfully added {first_name}')
        except:
            con.rollback()
        con.close()

    def viewNames(self):
        try:
            cursor.execute('SELECT * FROM payroll')
            details = cursor.fetchall()
            for detail in details:
                print(detail)
        except:
            con.rollback()
        con.close()

    def viewName(self, id):
        try:
            cursor.execute(f'SELECT * FROM payroll WHERE id = {id}')
            details = cursor.fetchone()
            print(details)
        except:
            con.rollback()
        con.close()

    def update(self):
        print('Check the row number before updating \t These are the column names you can update:')
        print('first_name')
        print('last_name')
        print('company_id')
        print('position')
        print('salary')
        print('\t')
        id = input('ID: ')
        column = input('Enter column: ')
        update = input('Enter update: ')
        try:
            cursor.execute(f"UPDATE payroll SET {column}='{update}' WHERE id={id}")
            con.commit()
            print('Successful operation')
        except:
            con.rollback()
        con.close()

    def delete(self, id):
        try:
            cursor.execute(f'DELETE FROM payroll WHERE id = {id}')
            con.commit()
            print('Successfully deleted')
        except:
            con.rollback()
        con.close()


while True:
    con = mysql.connector.connect(host='localhost', user='root', passwd='kambok123', database='nelson')
    cursor = con.cursor()
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')

    nelson = NelsonPay()

    print('\t')
    print('Welcome to NELSONPAY')
    print('\t')
    print('1.Add Details')
    print('2.View All')
    print('3.View Single')
    print('4.Update')
    print('5.Delete')
    print('\t')
    key = int(input('Enter Option: '))

    if key == 1:
        print('\t')
        nelson.addNames()
    if key == 2:
        print('\t')
        nelson.viewNames()
    if key == 3:
        print('\t')
        print('Enter Id Number')
        id_no = int(input('Enter Id: '))
        print('\t')
        nelson.viewName(id_no)
    if key == 4:
        print('\t')
        nelson.update()
    if key == 5:
        print('\t')
        id_no = int(input('Enter Id: '))
        nelson.delete(id_no)

    print('\n Do you want to continue? y/n')
    answer = input()
    if answer != 'y':
        break



