import requests

key = '3717556d5319562f74671847738e703e'
url = 'http://apis.juhe.cn/idcard/index'
data = {
    'cardno': '130929199108120939',
    'dtype': 'json',
    'key': key
}
req = requests.get(url, data)
content = req.json()
