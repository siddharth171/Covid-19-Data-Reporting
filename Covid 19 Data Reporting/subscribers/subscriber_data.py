import json

def get_subscriber_data():
    '''
    Loading subscribers data from json file
    '''
    print('Step 6: Getting subscriber data')
    
    # load subs json data, map count data to subs
    fd = open("subscribers\\subscription_data.json")
    subscription_data = json.load(fd)
    
    return subscription_data

