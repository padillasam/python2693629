import requests
import json

url="https://httpbin.org/get"#?nombre=juan&documento=12345"
response=requests.get(url)
#print(response.content.decode())
decodetest=response.content.decode()
print(type(decodetest))
print(response.json())
print('*'*20)
decodetestjson=json.loads(response.content)
print(decodetestjson)
print('*'*20)
print(decodetest)

# print(response.content.decode())
# print(type(response.content.decode()))
# jsonresponse=json.loads(response.content)
# print(type(jsonresponse))
