num = 5
#Right-angle triangle-upper
for i in range(1,num+1):
    print('*'*i)

print('\n')

#Right-angle triangle-lower
for i in range(0,num):
    print('*'*(num-i))

print('\n')

#Right-angle triangle-upper opposite
for i in range(1,num+1):
    print(' '*(num-i)+'*'*i)

print('\n')

#Right-angle triangle-lower opposite
for i in range(0,num):
    print(' '*i+'*'*(num-i))

print('\n')

#Triangle-upper
for i in range(1,num+1):
    print(' '*(num-i)+'* '*i)

print('\n')

#Triangle-lower
for i in range(0,num):
    print(' '*i+'* '*(num-i))

print('\n')

#Diamond shape
for i in range(1,num+1):
    print(' '*(num-i)+'* '*i)
for i in range(1,num):
    print(' '*i+'* '*(num-i))
print('\n')

#Pointed triangle
for i in range(1,num+1):
    print('* '*i)
for i in range(1,num):
    print('* '*(num-i))

print('\n')

#X shape
for i in range(num):
    print(' '*i+'* '*(num-i))
for i in range(num):
    print(' '*(num-i-1)+'* '*(i+1))

print('\n')

