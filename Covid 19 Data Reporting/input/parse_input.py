import requests



def process_api_data(input_url):
    '''
    Converting json data to dictionary
    Steps:
        1. Getting the jason data from the URL
            input url: https://data.covid19india.org/state_district_wise.json
        2. Dictionary data from json data
    '''
    
    print('Step 1: Get API data from json, URL: ', input_url)
      
    response = requests.get(input_url)
    states_map = response.json()
    print("Step 2: Sending data as dictionary")
    
    return states_map
    
def do_some_calc():
    '''
    Write Doc
    '''
    pass