import requests
 
res = requests.post('http://127.0.0.1:8002/hello/', data={'a':2, 'b':6})
print(res.text)