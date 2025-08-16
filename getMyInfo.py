import requests

token = "vHHePUP9_8pWLfIP5l6vcBR5h0StsdTMAAAAAQoNDV8AAAGX3f0KftIOHznOlwLN"
bearer_token = "Bearer "+ token
url = "https://kapi.kakao.com/v2/user/me"
headers = {
    "Authorization": bearer_token,
    "Content-Type":"application/x-www-form-urlencoded;charset=utf-8"
}

response = requests.get(url=url, headers=headers)
print(response.status_code)
print(response.text)