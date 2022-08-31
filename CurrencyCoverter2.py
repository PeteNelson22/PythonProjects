amt = int(input('Enter the amount '))
def exchange(amt):
    def naira(amt):
        print('NAIRA:',amt*600)
    def rupee(amt):
        print('RUPEE:',amt*100)
    def cedi(amt):
        print('CEDI:',amt*60)
    def cefa(amt):
        print('CEFA:',amt*30)

    naira(amt)
    rupee(amt)
    cedi(amt)
    cefa(amt)

exchange(amt)