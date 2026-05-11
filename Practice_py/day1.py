#--print("Hi Data engineer you are on the way")

name=input("Enter your name")
age=int(input("Enter your age"))
salary=int(input("Enter your expected salary"))

print(f"name:{name}")
print(f"age:{age}")
print(f"salary:{salary}")
print("The expected salary in EU is $70000")

if salary>=50000:
    print("You are blue card eligible")
else:
    print("You must keep trying")

years_to_eu=2
eu_age= age + years_to_eu

print(f"You'll be in EU in {eu_age} years")
