import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_number_info(phone_number):
    # Parse phone number
    parsed_number = phonenumbers.parse(phone_number)
    
    # Get country and location
    country = geocoder.country_name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "en")
    
    # Get carrier info
    phone_carrier = carrier.name_for_number(parsed_number, "en")
    
    # Get time zones associated with the phone number
    time_zones = timezone.time_zones_for_number(parsed_number)
    
    # Check if the phone number is valid and possible
    valid = phonenumbers.is_valid_number(parsed_number)
    possible = phonenumbers.is_possible_number(parsed_number)
    
    # Display the gathered information
    info = {
        "Phone Number": phone_number,
        "Country": country,
        "Location": location,
        "Carrier": phone_carrier,
        "Time Zones": time_zones,
        "Valid": valid,
        "Possible": possible
    }
    
    return info

# Ask the user to input the phone number
phone_number = input("Enter the phone number (with country code, e.g., +14155552671): ")

# Get phone number info
info = get_phone_number_info(phone_number)

# Print the information
for key, value in info.items():
    print(f"{key}: {value}")
