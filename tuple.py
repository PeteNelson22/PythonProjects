# # 1
# # tuple1=()
# # i=0
# # result=0
# # while i<10:
# #     tup = tuple(input("Enter the tuple elements ..."))
# #     result=tuple1+tup
# #     tuple1+=tup
# #     print(result)
#
# #2
# # tuple1=tuple(input('Enter a tuple without comma: '))
# # for i in tuple1:
# #     print(i)
#
# #9
# # name=input('Enter name: ')
# # age=int(input('Enter age: '))
# # sal=float(input('Enter salary: '))
# # org=input('Enter company: ')
# #
# # result=(name,age,sal,org)
# # print(result)
#
# #10
# # tuple1=tuple(input('Enter a sequence'))
# # print(tuple1)
# # print(tuple1[0])
#
# #11
# # tuple1=tuple(input('Enter a sequence'))
# # print(tuple1[4]+tuple1[1])
#
# # sandra = {'Name':'Ehi','age':'21','single':'true'}
# # print(sandra)
# # sandra['Name']='Sandra'
# # print(sandra)
# # #print(sandra['Name'])
# # import operator
# # d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # print('Original dictionary : ',d)
# # sorted_d = sorted(d.items(), key=operator.itemgetter(1))
# # print('Dictionary in ascending order by value : ',sorted_d)
# # sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# # print('Dictionary in descending order by value : ',sorted_d)
#
# import mysql.connector
# mycon = mysql.connector.connect(host="localhost",user="root",passwd="NELSON22")
# print(mycon)
import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",passwd="NELSON22")

print(myconn)