def function1():
    file_name=open("bank_data.txt","r")
    content=file_name.read()
    print(content)
    file_name.close()

function1()

def function2():
    filename=open("bank_data.txt","r")
    lines=filename.readlines()

    for line in lines:
        print(line)

    filename.close()

function2()    

def function3():
    count=0
    filename=open("bank_data.txt","r")
    lines=filename.readlines()

    for line in lines:
        count+=1
    print(f"Total banks is: {count} ")

    filename.close()

function3()    

def function4():
    filename=open("bank_data.txt","r")
    lines=filename.readlines()

    for line in lines:
        parts=line.split(",")
        print(parts[0])
    filename.close()

function4()    

def function5():
    filename=open("ca.csv", "r")
    lines=filename.readlines()

    for line in lines[1:]:
        parts=line.strip().split(",")
        if(parts[1]=="CA"):
            print(f"{parts[3]} | {parts[1]} | balance: Rs.{parts[2]}")
    filename.close()

function5()

def function6():
    filename=open("bank_data.txt", "r")
    content=filename.readlines()
    fully_compliant=0
    partially_compliant=0
    non_compliant=0

    for line in content:
        parts=line.strip().split(",")
        lcr=int(parts[1])
        nsfr=int(parts[2])
        if(lcr>=100 and nsfr>=100):
            status="Fully compliant"
            fully_compliant+=1
        elif((lcr>=100 and nsfr<=100) or (lcr<=100 and nsfr>=100)):
            status="Partially compliant"
            partially_compliant+=1
        else:
            status="Non compliant"
            non_compliant+=1

        print(f"{parts[0]} -> {status}")

    print(f"Fully compliant banks: {fully_compliant}")
    print(f"Partially compliant banks: {partially_compliant}")
    print(f"Non compliant banks: {non_compliant}")

function6()    






