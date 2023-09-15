def atm(balance):

    balance+=5

    return balance*2

new_value=int(input("What is your balance: "))

mybalance = atm(new_value)

print(mybalance)