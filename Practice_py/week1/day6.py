def function1():
    dict={"name":"Rahul", "age":"35", "designation":"Devops Engineer"}
    dict["department"]="DevOps"
    print(dict)
    print(type(dict))
    print(dict.get("name"))
    print(dict.keys())
    print(dict.values())
    print(dict.items())
    print(dict["age"])
    print(dict.update({"age" : "26"}))
function1()


bank={"bank_name":"HDFC", "lcr_ratio":123.7, "nsfr_ratio":456.7,"is_rbi_compliant":True}
print(bank)
print(bank.keys())
if bank["lcr_ratio"]>80:
    print(f"{bank["bank_name"]} - Safe and ok ")
else:
    print(f"{bank["bank_name"]} - Not ok.. ")

def function2():
    banks=[{"bank_name":"Deutsche Bank", "lcr_ratio":110, "nsfr_ratio":85},
           {"bank_name":"HDFC Bank", "lcr_ratio":120, "nsfr_ratio":300},
           {"bank_name":"HSBC Bank", "lcr_ratio":291, "nsfr_ratio":378},
           {"bank_name":"Barclays", "lcr_ratio":75, "nsfr_ratio":60}]
    
    for bank in banks:
        if(bank["lcr_ratio"]>=100 and bank["nsfr_ratio"]>=100):
            print(f"{bank["bank_name"]}: Fully compliant ✅")
        elif(bank["lcr_ratio"]>=100 or bank["nsfr_ratio"]>=100):
            print(f"{bank["bank_name"]} : Partially compliant ⚠️")
        else:
            print(f"{bank["bank_name"]} : Non compliant ❌")    
function2()                   