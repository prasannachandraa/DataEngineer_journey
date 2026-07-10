from collections import Counter
countries = ["Germany", "India", "Germany", "Netherlands", "India", "Germany"]
country__set=Counter(countries)
print(country__set)

banks = ["HDFC", "SBI", "AXIS", "ICICI", "PNB"]
long_names = [bank for bank in banks if len(bank) > 4]
print(long_names)  # print outside!!


from collections import defaultdict
employee_data = [
    ("Engineering", "Prasanna"),
    ("Sales", "Rahul"),
    ("Engineering", "Amit"),
    ("Sales", "Vikram")
]
#employee_ledger=defaultdict(employee_data)-- wrong usage should use list
employee_ledger=defaultdict(list)
#for employee, data in employee_ledger: -- wrong usage should iterate over data
for employee, data in employee_data:
    #employee_ledger[employee].append(amount) -- wrong variable
    employee_ledger[employee].append(data)
print(dict(employee_ledger))

from collections import defaultdict
cloud_logs = [
    {"region": "EU-West", "service": "EC2", "cost": 120},
    {"region": "IN-East", "service": "S3", "cost": 45},
    {"region": "EU-West", "service": "EC2", "cost": 300},
    {"region": "IN-East", "service": "EC2", "cost": 150},
    {"region": "EU-West", "service": "S3", "cost": 90}
]
cloud_data=defaultdict(list)
for log in cloud_logs:
    region_i=cloud_logs.get('region')
    cost_i=cloud_logs.get('cost')

    cloud_data[region_i].append(cost_i)
print(dict(cloud_logs))



#import response
import requests
def fetch_shipping_logs():
    url='https://api.euroshipments.nl/v2/tracking'
    request_header={
        #'header_key':"Authorization",
        #'header_value':"Bearer EURO_TRUCK_77"
        'Authorization':"Bearer EURO_TRUCK_77"
    }

    try:
        response=requests.get(url, headers=request_header)
        response.raise_for_status()

        data=response.json()
        print('The data received successfully')
        return data
    except requests.Except.HTTPError as httperr:
        print(f'Logistics Pipeline Broken: {httperr}')

    except Exception as err:
        print(f"General System Error Occurred: {err}")
