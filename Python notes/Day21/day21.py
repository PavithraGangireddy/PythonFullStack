#Authentication using PIN
correct_pin = 9812
pin = int(input("Enter your PIN: "))
if pin == correct_pin:
    print("Authentication successful")
else:
    print("Invalid PIN")

#check ATM pin
pin = int(input("Enter PIN: "))
if pin == 9812:
    print("PIN is correct")
else:
    print("Invalid PIN")

#cash deposit
balance = 10000
deposit = float(input("Enter deposit amount: "))
if deposit > 0:
    balance += deposit
    print("Cash deposited successfully")
    print("Current Balance:", balance)
else:
    print("Invalid deposit amount")

#cash withdrawal
balance = 10000
withdraw = float(input("Enter withdrawal amount: "))
if withdraw <= balance:
    balance -= withdraw
    print("Please collect your cash")
    print("Remaining Balance:", balance)
else:
    print("Insufficient balance")

# multiple PIN attempts
correct_pin = 9812
attempts = 3
for i in range(attempts):
    pin = int(input("Enter your PIN: "))
    if pin == correct_pin:
        print("PIN verified successfully")
        break
    else:
        print("Invalid PIN")
else:
    print("Account blocked due to multiple incorrect attempts")

#Withdrawal With Minimum Balance
balance = 10000
minimum_balance = 1000
withdraw = float(input("Enter withdrawal amount: "))
if withdraw <= 0:
    print("Invalid withdrawal amount")
elif balance - withdraw >= minimum_balance:
    balance -= withdraw
    print("Please collect your cash")
    print("Remaining Balance:", balance)
else:
    print("Withdrawal not allowed")
    print("Minimum balance of ₹1000 must be maintained")

#function for PIN verification
def verify_pin():
    correct_pin = 9812
    pin = int(input("Enter your PIN: "))
    if pin == correct_pin:
        return True
    else:
        return False
if verify_pin():
    print("PIN verified successfully")
else:
    print("Invalid PIN")

#ATM Transaction Balance History
balance = 10000
history = []
deposit = float(input("Enter deposit amount: "))
balance += deposit
history.append("Deposited: ₹" + str(deposit))
withdraw = float(input("Enter withdrawal amount: "))
if balance - withdraw >= 1000:
    balance -= withdraw
    history.append("Withdrawn: ₹" + str(withdraw))
else:
    print("Minimum balance must be maintained")
print("\nTransaction History:")
for transaction in history:
    print(transaction)
print("Current Balance:", balance)
