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
    except requests.exceptions.HTTPError as httperr:
        print(f'Logistics Pipeline Broken: {httperr}')

    except Exception as err:
        print(f"General System Error Occurred: {err}")

fetch_shipping_logs()


def fetch_inventory_dump():
    dump_data=inventory_dump.get('data', {})
    categories_list=dump_data.get('categories', [])
    for category in categories_list:
        items_list=category.get('items', [])
        for item in items_list:
            product_id=item.get('prod_id')
            price_i=item.get('price')
    
    print(f'product_id is: {product_id} | price is: {price_i}')

fetch_inventory_dump()


def parse_system_logs(filename):
    with open (filename, 'r') as file1:
        read_data=file1.read()

        for read in read_data:
            if read in "ERROR:":
                print(f"The required error message has beeen caught")

parse_system_logs(app_status.log)


import requests
def fetch_bank_url():
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        print(f'Data received successfully')
        return data
    
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return []
    
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection failed — check internet!!")
        return []
    
    except requests.exceptions.Timeout:
        print(f"❌ Request timed out!!")
        return []

# Test it!!
url = "https://jsonplaceholder.typicode.com/users"
data = fetch_bank_data(url)