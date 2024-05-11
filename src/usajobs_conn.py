import requests
import configparser

########################
# Project Credentials
########################
config = configparser.ConfigParser()
config.read(r'credentials/keys.ini')

# API Key Information
api_key = config['usajobs']['usajobs_key']
user_email = config['usajobs']['user_email']

########################
# USAJobs Functions
########################
def return_joblist(keyword = '',
                   position_title = '',
                   loc = ''):
    # The API URL
    url = 'https://data.usajobs.gov/api/Search'

    # Headers required by USAJOBS API
    headers = {
        'Authorization-Key': api_key,
        'User-Agent': user_email
    }

    # These should be pulled based on the information from the LLM
    params = {
        'Keyword': 'engineering',
        'PositionTitle': 'engineer',
        'LocationName': 'Washington, DC'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
    except Exception as e:
        print(e)

    # Checking if the request was successful
    if response.status_code == 200:
        # Processing the response JSON
        data = response.json()
        print(data)
    else:
        print('Failed to retrieve data:', response.status_code)

if __name__ == '__main__':
    pass
    #return_joblist