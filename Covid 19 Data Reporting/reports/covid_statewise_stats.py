import requests
import json
# form json.decoder import JSONDecoder
import logging


logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

statewise_data = {}

try:
    '''Getting covid data using the api link
    link: "https://data.covid19india.org/state_district_wise.json"
    '''
    data = requests.get("https://data.covid19india.org/state_district_wise.json")
    statewise_data = data.json()
    state_name = "Karnataka"
except FileNotFoundError:
    logging.critical("File Not Found!!")
except json.decoder.JSONDecodeError:
    logging.error("JSON structure is not correct...")
    
    
def get_total_cases(state_name, statewise_data):
    '''Getting total cases using get_total_case()'''
    #print("STATE STATE STAET WUSE SUE WUSE WUSE WSIE DTA : ", statewise_data)
    count = 0
    
    #print("SSSSSSSSTTTTTTTTTTTTTTTAAAAAAAAAAAAAAAAAATTTTTTTTTTTTTTEEEEEEEEEE: ", statewise_data)
    
    for state, dist_data in statewise_data.items():
        if state not in state_name or not isinstance(dist_data, dict):
            continue
        
        for dist, dist_value in dist_data.items():
            if not isinstance(dist_value, dict):
                continue
            
            for d_name, d_value in dist_value.items():
                if not isinstance(d_value, dict):
                    continue
                
                for key, value in d_value.items():
                    if key == "active":
                        count = count + int(value)
                        
    #print("COOOOUUUUUNNNTTTTTTTT: ",count)
    return count
    