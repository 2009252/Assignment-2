import requests

def domain_search(domain_name):
    api_url = f"https://domains.google.com/v2alpha1/registrations/{domain_name}:checkAvailability"
