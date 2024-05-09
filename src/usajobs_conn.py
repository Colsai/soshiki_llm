import requests
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config.ini file
config.read(r'credentials/keys.ini')

if __name__ == '__main__':
    # Your API key and email associated with the API key
    api_key = config['usajobs']['usajobs_key']
    user_email = config['usajobs']['user_email']

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
