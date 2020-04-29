
balance = float(input("Enter how much you want to save: "))
if (balance < 0 ):
    print("Looks like you already have enough saved...")
    balance = 0
    payment = 1
else:
    payment = float(input("Enter how much you will save each period: "))
if (payment <= 0 ):
    print("Savings have to be positive, please enter a positive value: ")


print("Balance is", balance, "and payment is", payment)

num_remaining_pmts = (balance/payment)


print("You must make", num_remaining_pmts, "more payments.")