import csv


def data_check_validation():
    # 1. Use 'with open' to read. It automatically closes the file safely!
    with open("finacle_extract.txt", "r") as infile:
        lines = infile.readlines()

    # 2. Initialize our tracking dictionary and variables
    success_summary = {}

    # 3. Open the quarantine file for writing bad data
    with open("quarantine.csv", "w", newline="") as quarantinefile:
        writer = csv.writer(quarantinefile)

        for line in lines:
            # Clean spaces and split by comma into a list of columns
            res = line.strip().split(",")

            # Defensive Check: If row is completely empty, skip it
            if not line.strip():
                continue

            # Extract columns for cleaner code readability
            txn_id = res[0]
            account_id = res[1]
            raw_amount = res[2].strip()  # Clean spaces around amount if any
            status = res[3]

            # GAP 2 FIX: Empty validation check
            if account_id == "":
                writer.writerow(res)  # Write the clean list to CSV
                print(f"Processing {txn_id}: [QUARANTINE] Missing account ID")
                continue

            # GAP 3 FIX: Safe amount data-type casting
            try:
                amount = int(raw_amount)
            except ValueError:
                writer.writerow(res)
                print(
                    f"Processing {txn_id}: [QUARANTINE] Malformed amount found."
                )
                continue

            # BASEL III Business Logic Check
            if status == "SUCCESS" and amount >= 1000000:
                print(
                    f"Processing {txn_id}: [ALERT] {account_id} triggered Basel III High-Value check! Amount: {amount}"
                )

            # GAP 2 & FUNCTION AGGREGATION FIX: Dictionary running total tracking
            if status == "SUCCESS":
                print(
                    f"Processing {txn_id}: Processed {amount} for {account_id}"
                )

                # If account already exists in our dictionary, add to its total
                if account_id in success_summary:
                    success_summary[account_id] += amount
                # Otherwise, initialize it with the current amount
                else:
                    success_summary[account_id] = amount

        # End of loop processing
        print("\n--- FINAL ETL SUMMARY ---")
        print(f"Total Successful Funds Processed: {success_summary}")


# Run the function
data_check_validation()