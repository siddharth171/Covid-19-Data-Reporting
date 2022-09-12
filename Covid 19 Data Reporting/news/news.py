from news.deccan_news import get_news_data, scrape_deccan_herald

def get_news():
    
    '''
    Get the news
    '''
    print('Step 5: Getting the News')
    
    get_news_data()
    scrape_deccan_herald()