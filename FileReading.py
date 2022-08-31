import os
print('Create Directory')
print('Add a File')
print('Write to a file')
while True:
        enter=input('Enter name of the folder: ')
        os.mkdir(enter)
        print('Successfully Created a folder')
        enter1=input('Enter name of the file: ')
        path=open(f"C:\\Users\\DICKSON\\Documents\\PythonProjects\\{enter}\\{enter1}",'x')
        print('File successfully created')
        enter2=input('Write Something ')
        path1=open(f"C:\\Users\\DICKSON\\Documents\\PythonProjects\\{enter}\\{enter1}",'w+')
        path1.write(enter2)
        print('Done')
        path1.close()



