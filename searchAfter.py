import requests
import json

file = open('resultsList_test2.txt', 'r')
lines = file.readlines()
file.close()
print('the search results is consist of ' + str(len(lines)) + ' toekns')

file = open('config.json', 'r')
config = json.load(file)
file.close()
#print(config)
kakaoAK = config['KakaoAK']

prompt = '''
안녕?
'''


headers = {
    'Authorization' : 'KakaoAK ' + kakaoAK
    , 'Content-Type' : 'application/json'

}
data = {
    'prompt' : prompt
    , 'max_tokens' : 1000
    #, 'temparature' : 1
    #, 'top_p' : top_p
    #, 'n' : n
}
res = requests.post('https://api.kakaobrain.com/v1/inference/kogpt/generation', headers=headers, json=data)
print(res.status_code)
print(res.text)