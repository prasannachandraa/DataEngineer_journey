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