import json
import csv
# Function 1
def read_transactions(filename):
    # reads CSV
    # returns list of rows!!
    rows=[]
    with open (filename,'r') as file1:
        reader=csv.reader(file1)
        #return reader--> wrong
        next(reader)
        for row in reader:
            rows.append(row)
    return rows    

# Function 2
def validate_row(rows):
    # checks schema, empty, numeric
    # returns True/False!!
    if len(rows)<4:
        return False
    
    for value in rows:
        if value=="":
            return False
    
    amount=rows[2]
    try:
        amount=int(amount)
    except ValueError:
        return False
    
    return True


# Function 3
def remove_duplicates(rows):
    # uses SET to remove duplicate transaction_ids!!
    # returns unique rows only!!
    duplicate_rows=set()
    unique_elem=[]

    for row in rows:
        row_tuple=tuple(row)
        if row_tuple not in duplicate_rows:
            duplicate_rows.add(row_tuple)
            unique_elem.append(row)
    
    return unique_elem

# Function 4
def aggregate_by_bank(rows):
    # uses DICTIONARY
    # totals amount per bank!!
    # returns dict!!
    by_bank_total={}
    for row in rows:
        bank_name=row[0]
        amount=row[2]
        if bank_name in by_bank_total:
            by_bank_total[bank_name]+=int(amount)
        else:
            by_bank_total[bank_name]=int(amount)
    
    return by_bank_total



# Function 5
def write_summary_json(summary, filename):
    # writes aggregated result to JSON file!!
    #summary_json=json.load(filename)--wrong
    with open(filename, 'w') as file1:
        json.dump(summary, file1, indent=4)

# Function 6
def run_pipeline(filename):
    # orchestrates everything!!
    rows=read_transactions(filename)
    print(f"DEBUG — first row: {rows[0]}")  # add this!!
    print(f"DEBUG — total rows read: {len(rows)}")  # add this!!

    valid_rows=[]
    invalid_rows=0

    for row in rows:
        if validate_row(row):
            valid_rows.append(row)
        else:
            invalid_rows+=1

    unique_elem=remove_duplicates(valid_rows)
    
    summary=aggregate_by_bank(unique_elem)

    write_summary_json(summary, 'summary.json')
    
    print(f"Total rows is: {len(rows)}")
    print(f"Invalid rows is :{invalid_rows}")
    print(f"Valid rows is: {len(valid_rows)}")
    print(f"Unique elements are : {len(unique_elem)}" )
    print(f"summary is :{summary}")

run_pipeline('transaction.csv')
