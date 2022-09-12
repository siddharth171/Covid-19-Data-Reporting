from reports.covid_statewise_stats import get_total_cases
from subscribers.subscriber_data import get_subscriber_data


def generate_user_report(subscription_data, statewise_data):
    '''
    input/arguments : subscription_data, statewise_data
                      - subscription_data : read from json
                      - statewise_data : we get it from covid_statewise_stats
    '''
    
    print("Generating USER report.....")
    
    # print("uuussseerrr dddaatttaaa rerrrrreeeeppppooorrtttt: ", statewise_data)
    
    subscriber_mail_map = {}
    
    for mail_id, list_of_states in subscription_data.items():        
        temporary_list = []
        for state_name in list_of_states:
            total_cases = get_total_cases(state_name, statewise_data)
            subs_map = {state_name:total_cases}
            temporary_list.append(subs_map)
        subs_map = {mail_id:temporary_list}
        subscriber_mail_map.update(subs_map)
               
    print("====="*10)
    print(subscriber_mail_map)
    print("====="*10)
    
    for k,v in subscriber_mail_map.items():
        print(k, "===>", v)
    print("====="*10)
    
    return subscriber_mail_map

