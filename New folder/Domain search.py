import requests


def check_domain_availability(domain_name):
    api_url = f"https://api.domainsdb.info/v1/domains/search?domain={domain_name}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return False
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return False
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return False
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return False
    try:
        response = requests.get(api_url)
        data = response.json()

        if data['total'] > 0:
            print(f"Sorry, the domain '{domain_name}' is not available.")
        else:
            print(f"The domain '{domain_name}' is available!")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
