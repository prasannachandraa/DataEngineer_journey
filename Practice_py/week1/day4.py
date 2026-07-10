no_of_cust=int(input(f"Enter the number of customers"))
premium_count=0
high_count=0
normal_count=0

for i in range(no_of_cust):

    name=input(f"Enter the name")
    balance=int(input(f"Enter the balance"))


    if(balance>50000):
        print(name, "Premium")
        premium_count+=1


    elif(10000<=balance<50000):
        print(name, "High value") 
        high_count+=1

    else:
        print(name, "Normal")
        normal_count+=1

print("summmaryyyy")
print(f"No of premium customers is",premium_count)
print(f"No of high customers is",high_count)
print(f"No of normal customers is",normal_count)




