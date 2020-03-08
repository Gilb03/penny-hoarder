# Get info from user 
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

#Calculate # of payments that will be needed 
num_remaining_pmts = (balance/payment)

#Present information to user 
print("You must make", num_remaining_pmts, "more payments.")