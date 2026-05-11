#PROBLEM NUMBER_1
def problem1():
    banks=['HDFC', 'AUSmallFinace','Deutsche bank', 'IM', 'Axis']

    for bank in banks:
        print(f"Processing {bank} regulatory report")

        if(bank=='HDFC'):
            print("Major private Bank")
        else:
            print("Processing normally")

problem1()

#Problem2
def problem2():
    lcr_ratio=[95, 110, 88, 120, 75]

    for ratio in lcr_ratio:
        if(ratio>=100):
            print(f"{ratio} - PASS ✅")
        else:
            print(f"{ratio} - FAIL ❌")

problem2()