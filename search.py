import requests
import json

file = open('config.json', 'r')
config = json.load(file)
file.close()
#print(config)
ttbkey = config['ttbkey']

file = open('titleList.txt', 'r')
lines = file.readlines()
file.close()

results = {}
for titleLine in lines:
    searchKey = titleLine.strip()
    searchAPIUrl = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey='+ttbkey+'&Query='+searchKey+'&QueryType=Title&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101'

    searchResponse = requests.get(searchAPIUrl)
    print('#### searchKey :  '+searchKey)
    #print(searchResponse.status_code)
    #print(response.text)
    #print(response.json)

    searchItems = json.loads(searchResponse.text)['item']
    results.setdefault(searchKey, [])
    for searchItem in searchItems:
        lookupKey = searchItem['isbn']

        lookupAPIUrl = 'http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey='+ttbkey+'&itemIdType=ISBN&ItemId='+lookupKey+'&output=js&Version=20131101&OptResult=ebookList,usedList,reviewList'

        lookupResponse = requests.get(lookupAPIUrl)
        print('- lookupKey : '+lookupKey)
        #print(lookupResponse.status_code)

        lookupItem = json.loads(lookupResponse.text)['item'][0]
        lookupResult = {
            'isbn' : lookupKey,
            'title' : lookupItem['title'],
            'author' : lookupItem['author'],
            'publisher' : lookupItem['publisher'],
            'pubDate' : lookupItem['pubDate'],
            'description' : lookupItem['description'],
            'categoryName' : lookupItem['categoryName'],
            'itemPage' : lookupItem['subInfo']['itemPage'],
            'customerReviewRank' : lookupItem['customerReviewRank']
        }
        results[searchKey].append(lookupResult)

file = open('resultsList.txt', 'w')
results_to_json = json.dumps(results, ensure_ascii=False)
file.write(results_to_json)
file.close()
#print(results)