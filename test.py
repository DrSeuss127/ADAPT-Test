from newsapi import NewsApiClient
import json

api = NewsApiClient(api_key='b575efe42ace400b8178b767afca23aa')

top_headlines = api.get_top_headlines(country='ph')

everything = api.get_everything(q='bongbong marcos', language='en')

with open('everything.json', 'w') as fp: 
    json.dump(everything, fp, indent=4)

with open('top_headlines.json', 'w') as f:
    json.dump(top_headlines, f, indent=4)