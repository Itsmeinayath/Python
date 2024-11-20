import requests

# Function to fetch a random user's username and country from the Free API
def fetch_random_user_freeapi():
    # URL of the Free API endpoint
    url ="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    # Sending a GET request to the API
    response = requests.get(url)
    # Parsing the JSON response
    data =  response.json()
    # Checking if the response indicates success and contains user data
    if data["success"] and "data" in data:
        user_data = data["data"]
        # Extracting the username and country from the user data
        username = user_data["login"]["username"] 
        country = user_data["location"]["country"] 
        return username, country
    else:
        # Raising an exception if the API call was not successful
        raise Exception("Failed to fetch user data")

# Main function to execute the script
def main():
    try:
        # Fetching the username and country
        username, country = fetch_random_user_freeapi()
        # Printing the fetched username and country
        print(f"Username: {username}")
        print(f"Country: {country}")
    except Exception as e:
        # Printing the error message if an exception occurs
        print(f"Error: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
