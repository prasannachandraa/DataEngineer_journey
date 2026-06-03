import csv

def process_employee_data(filename):
    total_rows=0
    valid_rows=0
    invalid_rows=0
    empty_field=0
    invalid_salary=0
    schema_validation=0

    with open(filename, 'r') as file, \
         open('valid_employees.csv', 'w', newline="") as file1, \
         open('quarantine.csv', 'w', newline="") as file2: 


        reader=csv.reader(file)
        header=next(reader)
        expected=['EmpID','Name','Salary','Department']

        if header!= expected:
            print(f"Header mismatchh exists")

        header.append('Salary_category')

        writer=csv.writer(file1)
        writer1=csv.writer(file2)

        writer.writerow(header)
        writer1.writerow(header)

        for row in reader:
            total_rows+=1

            if len(row)!=4:
                writer1.writerow(row)
                print(f"Schema validation mismatch")
                schema_validation+=1
                continue
            
            has_empty=False
            for value in row:
                if(value==""):
                    has_empty=True
                    empty_field+=1

            if(has_empty):
                writer1.writerow(row)
                print(f"{row[0]}{row[2]} having empty value")
                continue

            try:
                row[2]=int(row[2])
            except ValueError:
                writer1.writerow(row)
                print(f"{row[0]}{row[2]} is not having numeric value")
                invalid_salary+=1
                continue
                
            if(row[2]>100000):
                status='High'
            elif(row[2]>=50000 and row[2]<100000):
                status='Medium'
            else:
                status='Low'

            row.append(status)
            writer.writerow(row)
            print(f"{row[0]} {row[2]} is a valid row")
            valid_rows+=1
                
        invalid_rows=(schema_validation + invalid_salary + empty_field)
                
        print(f"Total rows:{total_rows}")
        print(f"Valid rows :{valid_rows}")
        print(f"Invalid rows:{invalid_rows}")
        print(f"Empty field rows:{empty_field}")
        print(f"Invalid salary rows:{invalid_salary}")
        print(f"Schema invalid rows:{schema_validation}")

process_employee_data("employee_data.csv")






    


