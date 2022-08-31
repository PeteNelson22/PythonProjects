def findMissingNumber(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1,length+1):
        if i not in numbers:
            output.append(i)
            output.split(i)
    return output

listOfNumbers=input('Enter a set of numbers: ')
listOfNumbers.split()
print(findMissingNumber(listOfNumbers))