import requests
 
res = requests.post('http://127.0.0.1:8002/hello/', data={'a':1, 'b':4})
print(res.text)