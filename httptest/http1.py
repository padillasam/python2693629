import requests
url="http://httpstat.us/505"

response=requests.get(url)
print(type(response))
print('.................',response.status_code)
file=open("http/styles.css","wb")
file.write(response.content)
file.close()

