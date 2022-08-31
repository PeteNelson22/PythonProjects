while True:
    print("1. Dollars")
    print("2. Euro")
    print("3. Pounds")
    print("4. Cedis")
    print("5. Exit")

    def dollar(naira):
        dollars = naira / 600
        print(f'Amount in Cedis is {dollars}')

    def pound(naira):
        pounds = naira / 700
        print(f'Amount in Cedis is {pounds}')

    def euro(naira):
        euros = naira / 650
        print(f'Amount in Cedis is {euros}')

    def cedi(naira):
        cedis = naira / 60
        print(f'Amount in Cedis is {cedis}')

    choice = input('\n')

    if choice == "1":
        naira = int(input("Enter the naira\n"))

        dollar(naira)

    elif choice == "2":
        naira = int(input("Enter the naira\n"))

        pound(naira)

    elif choice == "3":
        naira = int(input("Enter the naira\n"))

        euro(naira)

    elif choice == "4":
         naira = int(input("Enter the naira\n"))

         cedi(naira)

    elif choice == "5":
        break

    else:
        print("More updates will come later")

