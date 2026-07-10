name=input(f"Enter your name")
age=int(input(f"Enter your age"))
account_balance=int(input(f"Enter your balance"))

print(f"You name is {name} and you are {age} years of age")
if(account_balance>50000):
    print("Premium customer")
elif(10000<=account_balance<=50000):
    print("High value customer")
else:
    print("Normal customer")

if(age<25):
    print("You are perfectly crazyyy.. young customer")