import requests

def get_ip_location(ip_address):
    """Get the country and city of an IP address using the ipapi API."""
    api_key = "YOUR_API_KEY"
    api_url = f"https://api.ipapi.com/{ip_address}?access_key={api_key}"

    response = requests.get(api_url)
    response_json = response.json()

    country = response_json["country_name"]
    city = response_json["city"]

    return country, city

if __name__ == "__main__":
    ip_address = "8.8.8.8"  # Google's public DNS server
    country, city = get_ip_location(ip_address)
    print(f"{ip_address} is located in {country}, {city}.")