def validate_row(columns):

    if len(columns)<4:
        return False
    
    for value in columns:
        if columns=="":
            print(f"[REJECT] Missing Network for {columns[0]}")
            return False
        
    try:
        amount=int([2])
    except ValueError:
        print(f"[REJECT] Bad Amount Data for {columns[0]}")
        return False  
    
    return True

    
def print_summary(summary_dicti):

    print(f"--- FINAL SWIFT SETTLEMENT REPORT ---")
    
    for network, amount in summary_dicti.items():
        print(f"Network: {network} | Total Settled: INR {amount}")


def swift_parser(file1, file2):
    lcr_summary={}

    with open('swift_feed.txt', 'r') as file1, open('rejected_payments.txt', 'w',newline="") as file2:

        raw_lines=file1.readlines()
        for line in raw_lines:
            if not line.strip():
                continue

            columns=line.strip().split("::")

        if validate_row(columns):
            network=columns[1]
            amount=int(columns[2])
            status=columns[3]

            if status=="SETTLED":

                if network in lcr_summary:
                    lcr_summary[network]+=amount
                else:
                    lcr_summary[network]=amount
        else:
            file2.write(line)
        
    print_summary('lcr_summary')

swift_parser('swift_feed.txt', 'rejected_payments.txt')


