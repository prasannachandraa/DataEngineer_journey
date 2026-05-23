import csv

def function1():
    with open("ca.csv", "r") as file:
        reader=csv.reader(file)
        next(reader)

        for read in reader:
            print(f"Account:{read[0]} | Type: {read[1]} | Balance: {read[2]} | Bank: {read[3]} ")

function1()

def function2():
    with open("ca.csv", "r") as file:
        reader=csv.reader(file)
        next(reader)
        total=0
        high_value=0

        for read in reader:
            if(read[1]=="CA"):
                balance=int(read[2])
                
                if(balance>500000):
                    status="High value"
                    high_value+=1
                else:
                    status="Regular"
                total+=1  

                print(f"Account:{read[0]} | Type: {read[1]} | Balance: Rs.{read[2]}  | Bank: {read[3]}  | Status: {status}")      

        print(f"Total CA accounts: {total}")
        print(f"High Value accounts: {high_value}")
    
function2()

import csv
import os

def validate_csv(filename):
    if os.path.exists(filename):
        print(f"filename : {filename} exists")
    else:
        print(f"filename : {filename} ❌ doesnt exists")
        return False
    
    if os.path.getsize(filename):
        print(f"filesize: {filename} is not empty")
    else:
        print(f"filesize: {filename} is empty")
        return False
    
    with open("ca.csv","r") as file:
        reader=csv.reader(file)
        header=next(reader)
        expected=["account_no","account_type","balance","bank_name"]

        if(header==expected):
            print(f"both header and reader are matching")
        else:
            print(f"Not matching")
    

        for row in reader:
            for value in reader:
                if(value==""):
                    print(f"{filename} is empty")
                    return False
                   

            if(row[2].isdigit)==True:   
                print(f"Balance is not numberic {row[2]}")
                return False
            
            print("All rows valid")
            return True
    
validate_csv("ca.csv")
validate_csv("ca1.csv")
    
def validation_csv():
    good_rows=[]
    quarantine=[]

    with open("ca.csv", "r") as file:
        validator=csv.validator(file)

        for value in validator:
            for row in reader:
                if(row==""):
                    quarantine.append(value)
                    print(f" Bad row: {validator[0]} {validator[3]} empty value!!")
                    quarantine+=1
                    return False
                
            if(value[2].isdigit)=="True":
                quarantine.append(value)
                print(f"❌ Bad row: {validator[0]} {validator[3]} — balance not numeric!!")
                quarantine+=1
                return False
            
            if is_valid(value):
                good_rows.append(value)
                print(f"Processing: {validator[0]} {validator[3]}")
                good_rows+=1

        print(f"📊 Summary:")
        print(f"✅ Processed:{good_rows}")
        print(f"⚠️ Quarantined: {bad_rows}")
        print("📁 Check quarantine.csv!!")

validation_csv(ca.csv)


            


