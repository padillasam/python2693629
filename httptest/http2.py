import requests
url="http://httpstat.us/505"
response=requests.get(url)
print(type(response))
print('.................',response.status_code)
if response.status_code>=200 and response.status_code<300:
    print(response.content)
elif response.status_code>=300 and response.status_code<400:
    print("Redirección")
elif response.status_code>=400 and response.status_code<500:
    print("Error en el cliente")
elif response.status_code>=500:
    print("Error en el servidor")