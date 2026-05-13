def practice1():
    attempts=0
    service_running=False


    while attempts<5:
        attempts+=1
        print(f"Attempt {attempts} checking executor services")
    
        if service_running==True:   
            print("Service running batch starting")
            break

    else:
        print("Alert service down contact Administrator")    

practice1()

def check_bank_compliance(lcr,nsfr):
    if(lcr>=100 and nsfr>=100):
        return "Fully compliant"
    
    elif((lcr>=100 and nsfr<=100)or (lcr<=100 and nsfr>=100)):
        return "Partially compliant"
    
    else:
        return "Non compliant"
    
lcr=int(input("Enter the lcr ratio"))
nsfr=int(input("Enter the nsfr ratio"))

result=check_bank_compliance(lcr,nsfr)

print(result)

def practice3():
    file_name="LCR_REPORT_2026.CSV"

    res=file_name.lower()
    print(res)

    res2=file_name.replace(".CSV","")
    print(res2)

    res3=file_name.split("_")
    print(res3)


practice3()

def practice4():
    banks=[ "  hdfc bank  ",
    "STATE BANK OF INDIA",
    "axis-bank",
    "  icici BANK  "]

    for bank in banks:
       res= bank.strip().upper().replace("-", " ")
       print(res)

practice4()

def practice5():
    file_name="LCR_REPORT_2026.CSV"

    res=file_name.lower().replace("_"," ").replace(".csv", " ")
    print(res)

practice5()
