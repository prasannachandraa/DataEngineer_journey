import csv
def bank_data_validation(filename):
    empty_field=0
    non_numeric=0
    schema_invalid=0
    duplicate=0
    valid_rows=0
    total_rows=0

    seen_rows=set()

    with open(filename,'r') as file, \
         open('results.csv', 'w', newline="") as results_file, \
         open('quarantine.csv', 'w', newline="") as quarantine_file, \
         open('summary.txt', 'w', newline="") as summary_file:
        
        reader=csv.reader(file)
        header=next(reader)

        expected = ["Bank", "City", "Balance", "Owner"]

        if header!=expected:
            print("Header schema mismatch")
            return
        
        header.append('Risk_category')

        writer=csv.writer(results_file)
        writer1=csv.writer(quarantine_file)

        writer.writerow(header)
        writer1.writerow(header)

        for row in reader:

            total_rows+=1
            if len(row)!=4:
                writer1.writerow(row)
                print(f"Invalid schema validation: {row} ")
                schema_invalid+=1
                continue

            has_empty=False
            for value in row:
                if(value==""):
                    has_empty=True
                    break

            if(has_empty):
                writer1.writerow(row)
                print(f"Bad row - {row[0]} {row[3]} - is empty")
                empty_field+=1
                continue

            if not(row[2].isdigit()):
                writer1.writerow(row)
                print(f"Bad row - {row[0]} {row[3]} - is non numeric")
                non_numeric+=1
                continue
            
            row_tuple=tuple(row)

            if (row_tuple) in seen_rows:
                writer1.writerow(row)
                print(f"Bad row - {row[0]} {row[3]} - is duplicate")
                duplicate+=1
                continue

            row[2]=int(row[2])
            if(row[2]>50000):
                status='High value'
            elif(1000<=row[2]<=5000):
                status='Medium'
            else:
                status='Low'    
        
            writer.writerow(row)

            valid_rows += 1

            print(f"✅ Processed row: {row[0]} {row[3]}")

        invalid_rows = (
            empty_field +
            non_numeric +
            schema_invalid +
            duplicate
        )

        # Summary report
        summary_file.write(f"Total rows processed: {total_rows}\n")
        summary_file.write(f"Valid rows: {valid_rows}\n")
        summary_file.write(f"Invalid rows: {invalid_rows}\n")
        summary_file.write(f"Empty field rows: {empty_field}\n")
        summary_file.write(f"Non numeric rows: {non_numeric}\n")
        summary_file.write(f"Schema invalid rows: {schema_invalid}\n")
        summary_file.write(f"Duplicate rows: {duplicate}\n")

        print("\n📊 Processing Complete!")
        print("✅ results.csv generated")
        print("⚠️ quarantine.csv generated")
        print("📝 summary.txt generated")

        
bank_data_validation("bank_data.csv")






                

