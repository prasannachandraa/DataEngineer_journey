import csv
def validate_salary(salary):
    #let me know if we shouldd do or not the schema validation
    
    
    for value in salary:
        if value=="":
            return False
        
    try:
        salary=int(salary)
    except ValueError:
        return False
    
    if salary<=0:
        return False
    
    
    return True

def run_pipeline(employees):
    valid_count=0
    invalid_count=0
    invalid_employees=[]

    for employee in employees:
        salary=employee['salary']
        name=employee['name']
            
        if not validate_salary(salary): 
            invalid_count+=1
            invalid_employees.append(name)
        else:
             valid_count+=1
        
    print_results(valid_count, invalid_count, invalid_employees)

run_pipeline(employees)



def print_results(valid_salary, invalid_salary, invalid_employee):
    print(f"Invalid count is {invalid_salary}") #for list how we need to invoke
    print(f"Valid salary is {valid_salary}")
    print(f"Invalid employees are: {invalid_employee}")
      






        