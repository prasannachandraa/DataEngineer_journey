# A raw list of successful transaction values processed by your pipeline
# Format: (Account_ID, Txn_Amount)
mock_transactions = [
    ("ACC_101", 5000),
    ("ACC_202", 12000),
    ("ACC_101", 3000),
    ("ACC_303", 45000),
    ("ACC_202", 1000),
]

# This is your empty ledger to track total balance per account
account_balances = {}

# We loop through our list of records
for account_id, amount in mock_transactions:
    # --- YOUR DE CHALLENGE IS HERE ---

    # 1. Write an 'if' statement to check if account_id is ALREADY in account_balances
    # Hint: if account_id in account_balances:
    if(account_id) in account_balances:

    # 2. If it IS there, add the current 'amount' to its existing balance
        account_balances[account_id]+=amount

    # 3. Write the 'else' statement for when the account is NOT there
    else:

    # 4. If it is NOT there, initialize it: account_balances[account_id] = amount
        account_balances[account_id]=amount

# Print the final ledger to check your work
print("Final Balances:", account_balances)


#def count_departments(employees):

    #department_list={}

    #for employee in employees:
        
    #    department=employee["dept"]

    #    if department in department_list:
    #        department_list[department]+=1
    #    else:
    #        department_list[department]=1
        
    #    return department_list


#count_departments(employees)

transactions = [
    {"bank": "SBI", "amount": 1000},
    {"bank": "HDFC", "amount": 2000},
    {"bank": "SBI", "amount": 500}
]

def calculate_bank_totals(transactions):
    final_derived={}

    for transaction in transactions:
        particular_trans=transaction["bank"]
        amount=transaction["amount"]

        if particular_trans in final_derived:
            final_derived[particular_trans]+=amount
        else:
            final_derived[particular_trans]=amount

    return final_derived

calculate_bank_totals(transactions)



        