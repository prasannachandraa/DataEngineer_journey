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