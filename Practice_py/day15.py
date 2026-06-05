import csv
def lcr_pipeline(filename):
    lcr_summary={}

    with open(filename, 'r') as lcrfilename:
        
        reader=lcrfilename.readlines()

        for row in reader:
            res=row.strip().split(",")

            # Fix 1 — schema check!!
            if len(res) < 3:
                print(f"❌ Bad row: {row.strip()}")
                continue

            amount=res[2]
            amount=amount.replace(","," ")
            category=res[0].lower()

            try:
                amount=int(amount)
            except ValueError:
                print(f"Invalid amount")
                continue

            if category in lcr_summary:
                lcr_summary[category]+=amount
            else:
                lcr_summary[category]=amount
        
    print(f"--- FINAL BASEL III LCR ASSET REPORT ---")
    for asset_class, total_value in lcr_summary.items():
        print(f"Asset class is {asset_class} and Total value is INR{total_value} ")

lcr_pipeline("lcr_assets.txt")

