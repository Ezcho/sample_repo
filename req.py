#간단하게 HTTP콜을 보내는 방법
import requests
url = "https://kauth.kakao.com/oauth/token"

headers={
    "Content-Type":"application/x-www-form-urlencoded;charset=utf-8"
}
body={
    "grant_type":"authorization_code",
    "client_id":"bb6d3c08e783d1b041142d4f2281b3a9",
    "redirect_uri":"http://127.0.0.1:5000/callback",
    "code":"E32BOhi-EE7IcZF45QKEAuE8RBmqi5RfBjFrRUzRsocd71eaPQAkGwAAAAQKDR-XAAABl932-m237mS5Kc-sjw",
    "client_secret":"vivFFbMrWKUIN2ncqqTSRoTvdb44IIDt"

}
try:
    response = requests.post(url=url,data=body,headers=headers)
    print(response.status_code)
    print(response.text)
except Exception as e:
    print("some issues..")
    print(e)




"""
"192.168.10.32"
url = "https://kauth.kakao.com/oauth/token"
path = "/add"
s = url+path

body = {"name":"jisan"}

response = requests.post(s, json=body)
print(response.text)
"""