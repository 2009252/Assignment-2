import requests

def check_domain_availability(domain_name):
    api_url = f"https://api.domainsdb.info/v1/domains/search?domain={domain_name}"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if data['total'] > 0:
            print(f"Sorry, {domain_name} is not available.")
            print("-------------------------------------------------------------")
            print("There are", data['total'], "Domains with this word used")
            print("-------------------------------------------------------------")
            print("First 20 results:")
            print("-------------------------------------------------------------")
            for result in data['domains'][:20]:
                print(result['domain'])
    else:
        print(f"Domain Name is availabile for: {domain_name}. Status code: The domain can not be found: {response.status_code}")

if __name__ == "__main__":
    user_input = input("Enter a domain name to check its availability: ")
    check_domain_availability(user_input)