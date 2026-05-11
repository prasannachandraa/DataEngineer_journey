bank_name=input(f"Enter the bank name")
operation_years=int(input(f"Enter the years of operation"))
total_deposits=int(input(f"Enter the total amount of deposits"))

print(f"Bank name:{bank_name} | Years:{operation_years}| deposits:{total_deposits}")
if(total_deposits>10000000):
    print("Its a Major bank")
else:
    print("Its a regional bank")