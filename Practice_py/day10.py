import csv
def validation_csv(filename):
    good_rows=[]
    quarantine=[]

    with open('ca.csv', "r") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            has_empty=False
            for value in row:
                if(value==""):
                    has_empty=True
                    break

            if (has_empty):
                quarantine.append(row)
                print(f"❌ Bad row: {row[0]} {row[3]} — empty value!!")
                continue

            if not (row[2].isdigit()):
                quarantine.append(row)
                print(f"❌ Bad row: {row[0]} {row[3]} — balance not numeric!!")  
                continue

            good_rows.append(row)
            print(f"✅ Processing: {row[0]} {row[3]}")

        print(f"📊 Summary:")
        print(f"✅ Processed:{good_rows}")
        print(f"⚠️ Quarantined: {quarantine}")
        print("📁 Check quarantine.csv!!")

validation_csv("ca.csv")

def write_csv(filename):
    good_rows=[]

    with open('ca.csv', "r") as filename, open('quarantine.csv', "w") as file1:
        reader=csv.reader(filename)
        
        writer=csv.writer(file1)
        header=next(reader)

        
        for row in reader:
            has_empty=False
            for value in row:
                if(value==""):
                    has_empty=True
                    break;
                
            if(has_empty):
                writer.writerow(row)
                print(f"❌ Bad row: {row[0]} {row[3]} — empty value!!")
                continue

            if not (row[2].isdigit()):
                writer.writerow(row)
                print(f"❌ Bad row: {row[0]} {row[3]} — not a digit!!")
                continue   

            good_rows.append(row)
            print(f"✅ Processing: {row[0]} {row[3]}")            



        print(f"📊 Summary:")
        print(f"✅ Processed:{good_rows}")
        print("📁 Check quarantine.csv!!")

write_csv("ca.csv")


def write_results(filename):
    quarantine=[]

    with open ('ca.csv', 'r') as filename, open('results.csv', 'w', newline="") as filename1:
        reader=csv.reader(filename)
        
        header=next(reader)
        header.append('status')
        writer=csv.writer(filename1)
        writer.writerow(header)

        for row in reader:
            has_empty=False
            for value in row:
                if(value==""):
                    has_empty=True
                    break;
                
            if(has_empty):
                    quarantine.append(row)
                    print(f"Bad row: {row[0]} {row[3]} has empty value")
                    continue

            if not (row[2].isdigit()):
                quarantine.append(row)
                print(f"Bad rows: {row[0]} {row[3]} - is not a digit")
                continue


            row[2]=int(row[2])
            if(row[2]>50000):
                row.append('High value')
            else:
                row.append('Regular')
            
            writer.writerow(row)
            print(f"Values Appended to results.csv - Check it")

write_results("ca.csv")             
                    

                


