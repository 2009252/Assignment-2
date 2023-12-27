import requests

def domain_search(domain_name):
    api_url = f"https://api.domainsdb.info/v1/domains/search?domain={domain_name}:checkAvailability"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
