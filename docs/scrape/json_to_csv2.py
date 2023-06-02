import json
import csv

# Load JSON data from file
with open('2023-06-02_twitter.json', 'r', encoding='utf-8') as file:
    data = file.read()
    data = data.strip().split('\n')
links_url = links_url2 = links_url3 = links_url4 = links_url5 = media_url = media_url2 = media_url3 = media_url4  = media_url5 =''
 # Extract desired information from JSON
rows = []
for json_str in data:
    item = json.loads(json_str)
    date = item['date']
    url = item['url']
    username = item['user']['username']
    raw_content = item['rawContent']
    if item['links'] is not None and len(item['links']) > 0:
        links_url = item['links'][0]['url']
    else:
        links_url = ''

    try:
        links_url2 = item['links'][1]['url']
    except:
        link_url2 = ""   

    try:
        links_url3 = item['links'][2]['url']
    except:
        link_url3 = ""

    try:
        links_url4 = item['links'][3]['url']
    except:
        link_url4 = ""   
    try:
        links_url5 = item['links'][4]['url']
    except:
        link_url5 = ""  

          
    if item['media'] is not None and len(item['media']) > 0:
        if 'fullUrl' in item['media'][0]:
            media_url = item['media'][0]['fullUrl']
        else:
            media_url = ''
    else:
        media_url = ''
    try:
        media_url2 = item['media'][1]['fullUrl']
    except:
        media_url2 = ""   

    try:
        media_url3 = item['media'][2]['fullUrl']
    except:
        media_url3 = ""

    try:
        media_url4 = item['media'][3]['fullUrl']
    except:
        media_url4 = ""   
    try:
        media_url5 = item['media'][4]['fullUrl']
    except:
        media_url5 = ""    
    
    rows.append([date, url, username, raw_content, links_url, links_url2, link_url3, link_url4, link_url5 , media_url, media_url2, media_url3, media_url4, media_url5])
    links_url = links_url2 = links_url3 = links_url4 = links_url5 = media_url = media_url2 = media_url3 = media_url4  = media_url5 =''
headers = ['date', 'url', 'username', 'content', 'link0', 'link1', 'link2', 'link3', 'link4', 'url0', 'url1', 'url2', 'url3', 'url4']
with open('2023-06-02_twitter.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)
