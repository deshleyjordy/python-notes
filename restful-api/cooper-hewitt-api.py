import requests

url = "https://api.collection.cooperhewitt.org/rest/?method=cooperhewitt.search.objects&query=clock%20radio&page=1&per_page=100&access_token=b57af8373b6020684f258c2ce3524c06"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, verify=False)

print(response.text.encode('utf8'))