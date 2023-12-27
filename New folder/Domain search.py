import requests

def domain_search(domain_name):
    api_url = f"https://domains.google.com/v2alpha1/registrations/{domain_name}:checkAvailability"


    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return False
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return False
