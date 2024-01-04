import requests


def check_domain_availability(domain_name):
    api_url = f"https://api.domainsdb.info/v1/domains/search?domain={domain_name}"

       try:
        response = requests.get(api_url)
        data = response.json()

        if data['total'] > 0:
            print(f"Sorry, the domain '{domain_name}' is not available.")
        else:
            print(f"The domain '{domain_name}' is available!")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
