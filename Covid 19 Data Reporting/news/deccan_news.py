import requests
import re
import json
from bs4 import BeautifulSoup


NEWS_URLS = {
    "The Hindu": "https://www.thehindu.com/",
    "Deccan Herald": "https://www.decccanherald.com/"
}

def get_news_data():
    '''
    Collecting news....
    '''
    print("Collecting News....")

    # Scrape DH news website
    news_map = scrape_deccan_herald()  
    return news_map


def scrape_deccan_herald():
    '''
    Scraping news from Deccan Herald
    '''
    print("Scraping Deccan Herald....")
    main_url = "https://www.deccanherald.com"
    page = requests.get(main_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    news_map = {} # hyper link: news text
    
    all_urls = soup.find_all("a", href=re.compile("(?!)corona|covid")) # ignore case
    all_urls = list(set(all_urls)) # remove duplicates
    
    for url in all_urls:
        sub_url = url['href']
        sub_page = requests.get(main_url + sub_url)
        sub_soup = BeautifulSoup(sub_page.content, 'html.parser')
        news_content = sub_soup.find_all("script", type="application/ld+json")
        for news in news_content:
            news_content_json = json.loads(news.text) # this is json
            if "articleBody" in news_content_json.keys() and "headline" in news_content_json.keys():
                news_map.update({main_url+sub_url : news_content_json["headline"]})
    
    if len(news_map) == 0:
        print("Deccan Herald: No News Found!")
    
    from pdb import set_trace
    # set_trace()
    for k,v in news_map.items():
        print("========================"*6)
        print("key: ", k)
        print("value: ", v)
    
    return news_map

if __name__ == '__main__':
    get_news()