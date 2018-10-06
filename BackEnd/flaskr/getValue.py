import requests
import json
from requests.auth import HTTPBasicAuth


def getContent(name):
    url = 'https://api.imagga.com/v1/content'
    headers = {'Authorization': 'Basic YWNjX2E5N2E0ZWJkYzUxNzRhYjoyM2QwM2FiYjA5YWQ2M2FjZDEzZDA5MzEwOWQ4ZmMzMw=='}
    files = {'image': open('static/' + name)}

    print(files)
    r = requests.post(url, files=files, headers=headers)
    getTagging(json.loads(r.content)['uploaded'][0]['id'])
    
def getTagging(id):
    
    param = {'content': '5274d8112ad5110fa035098503ada450'}
    r2 = requests.get(url = 'https://api.imagga.com/v1/tagging', auth=HTTPBasicAuth('acc_a97a4ebdc5174ab', '23d03abb09ad63acd13d093109d8fc33'), params=param)

    r = json.loads(r2)
    tag_list = r['results']['tags']
    
    # x = requests.request('GET', 'https://api.imagga.com/v1/tagging', params=param)
    print(r2.content)
    # print(r3)


getContent('used shoes.jpg')
