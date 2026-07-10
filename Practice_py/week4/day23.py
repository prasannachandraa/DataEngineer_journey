import requests
def fetch_bank_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Fetched {len(data)} records!!")
        return data
    
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        # Log to file!!
        with open("api_errors.log", "a") as log:
            log.write(f"HTTP Error: {e}\n")
        return []
    
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection failed!!")
        with open("api_errors.log", "a") as log:
            log.write(f"Connection failed for {url}\n")
        return []