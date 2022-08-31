a=int(input("enter a num"))

def checkNum(a):
    for i in range(2,a):
        if a%i==0:
            return False

    return True


print(checkNum(a))

