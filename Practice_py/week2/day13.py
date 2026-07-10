def scenario2():
    salaries = ["50000", "ABCDEF", "75000", "NULL", "90000"]
    
    for row in salaries:
        try:
            result = int(row)
            print(f"✅ Valid salary: {result}")
        except ValueError:
            print(f"❌ Invalid: {row}")
            continue

scenario2()
