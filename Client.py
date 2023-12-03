import requests, json

url='http://192.168.1.254:7770/data'

res = requests.get(url)

res = res.text
res = json.loads(res)

res=res['amount']

print("\n",res,"\n")