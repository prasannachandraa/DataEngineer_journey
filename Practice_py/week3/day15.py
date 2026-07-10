import csv
def lcr_pipeline(filename):
    lcr_summary={}

    with open(filename, 'r') as lcrfilename:
        
        reader=lcrfilename.readlines()

        for row in reader:
            res=row.strip().split(",")

            # Fix 1 — schema check!!
            if len(res) < 3:
                print(f"❌ Bad row: {row.strip()}")
                continue

            amount=res[2]
            amount=amount.replace(","," ")
            category=res[0].lower()

            try:
                amount=int(amount)
            except ValueError:
                print(f"Invalid amount")
                continue

            if category in lcr_summary:
                lcr_summary[category]+=amount
            else:
                lcr_summary[category]=amount
        
    print(f"--- FINAL BASEL III LCR ASSET REPORT ---")
    for asset_class, total_value in lcr_summary.items():
        print(f"Asset class is {asset_class} and Total value is INR{total_value} ")

lcr_pipeline("lcr_assets.txt")

import csv
def validate_row(row):
    if len(row)<4:
        return False
    
    for value in row:
        if value=="":
            return False
    try:
        int(row[2])
    except ValueError:
        return False
    
    return True


def transform_row(row):
    salary=int(row[2])

    if(salary>100000):
        status='High salary'
    elif(salary>=50000):
        status='Medium salary'
    else:
        status='Low salary'
    
    row.append(status)
    return status

def write_output(rows, filename):
    with open(filename, 'w', newline="") as file1:
        writer=csv.writer(file1)
        for row in rows:
            op_result=writer.writerow(row)
        
        return op_result
    
def print_summary(total, valid, invalid):
    print(f"Total is {total}")
    print(f"Total valid is : {valid}")
    print(f"Total invalid is {invalid}")


def run_pipeline(filename):
    total=0
    valid=[]
    invalid=0

    with open(filename, 'r') as file1:
        reader=csv.reader(file1)

        for row in reader:
            total+=1

            if validate_row(row):
                transform=transform_row(row)
                valid.append(transform)
            else:
                invalid+=1
            
    write_output(valid, "output.csv")
    print_summary(total, len(valid), invalid)



    


run_pipeline('employee_data.csv')


