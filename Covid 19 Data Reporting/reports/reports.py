from input.parse_input import process_api_data
from news.news import get_news
from subscribers.subscriber_data import get_subscriber_data
from mail.send_mail import send_mail
from reports.generate_xls import generate_xls_report
from reports.generate_user_report import generate_user_report
from reports import covid_statewise_stats

def process_state_data():
    '''
    Getting the news data by webscraping
    '''
    print('Step 3: Get statewise data')
    
def process_xls_report(data):
    '''
    Write Doc
    '''
    print('Step 4: Make XLS report')
    generate_xls_report(data)
    
def process_news():
    '''
    Write Doc
    '''
    print('Step 5: Process news')
    
# AGGREGATING

def aggregate():
    
    '''
    URL is save as a variable
    Then we aggregate the interfaces
    '''
    URL = "https://data.covid19india.org/state_district_wise.json"
    
    # GETTING API DATA
    api_data = process_api_data(URL)
    print("==="*48)
    print("length of Data",len(api_data))
    print("==="*48)
    
    # PROCESSING API DATA
    process_state_data()
    
    # GENERATING EXCEL REPORT
    process_xls_report(api_data)
    
    # GETTING NEWS FROM NEWS WEBSITES
    get_news()
    process_news()
    
    # GETTING SUBSCRIBERS DATA
    subs_map = get_subscriber_data()
    print("subs_map", subs_map)
    
    #print("aaaaaaaaaaaaaaaaaapppppppppppppiiiiiiiiiii dddddaaaaattttaaaa: ", api_data)
    
    # GENERATING USER REPORT
    # all_states = api_data.keys()
    # state_stats_map = {}
    # for state_name in all_states:
    #     total_cases = covid_statewise_stats.get_total_cases(state_name, api_data)
    #     state_stats_map.update({state_name: total_cases})
    
    generate_user_report(subs_map, api_data)
    
    print("Step 7: Aggregated data")    
    send_mail()