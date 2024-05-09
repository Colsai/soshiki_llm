import requests

if __name__ == '__main__':
    # Your API key and email associated with the API key
    api_key = 'TLhMOf9i7evIDxptFhKAtYGHQrwi+6Wyi3QHrMc8QrA='
    user_email = 'schirabay@gmail.com'

    # The API URL
    url = 'https://data.usajobs.gov/api/Search'

    # Headers required by USAJOBS API
    headers = {
        'Authorization-Key': api_key,
        'User-Agent': user_email  # This should be the email associated with your API key
    }

    # Parameters for the API call, for example, searching for jobs by keyword, location, etc.
    params = {
        'Keyword': 'engineering',
        'PositionTitle': 'engineer',
        'LocationName': 'Washington, DC'
    }

    # Making the GET request
    response = requests.get(url, headers=headers, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        # Processing the response JSON
        data = response.json()
        print(data)
    else:
        print('Failed to retrieve data:', response.status_code)