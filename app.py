from flask import Flask, redirect, request, jsonify,render_template
import requests
import json

app = Flask(__name__)


        


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/callback")
def callback():
    code = request.args.get('code')
    url = "https://kauth.kakao.com/oauth/token"

    headers={
        "Content-Type":"application/x-www-form-urlencoded;charset=utf-8"
    }
    body={
        "grant_type":"authorization_code",
        "client_id":"bb6d3c08e783d1b041142d4f2281b3a9",
        "redirect_uri":"http://127.0.0.1:5000/callback",
        "code": code,
        "client_secret":"vivFFbMrWKUIN2ncqqTSRoTvdb44IIDt"

    }
    try:
        response = requests.post(url=url,data=body,headers=headers)
        response = response.json()
        access_token = response['access_token']
        print(access_token)
    except Exception as e:
        print("some issues..")
        print(e)
    
    try:
        bearer_token = "Bearer "+ access_token
        url = "https://kapi.kakao.com/v2/user/me"
        headers = {
            "Authorization": bearer_token,
            "Content-Type":"application/x-www-form-urlencoded;charset=utf-8"
        }
        response = requests.get(url=url, headers=headers)
        print(response.status_code)
        print(response.text)
    except Exception as e:
        print("some issues..")
        print(e)
    response = response.json()
    email = response['kakao_account']['email']
    nickname = response['kakao_account']['profile']['nickname']
    print(email, nickname)

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    bearer_token = "Bearer "+ access_token
    headers = {
        "Authorization": bearer_token,
        "Content-Type":"application/x-www-form-urlencoded;charset=utf-8"
    }
        
    template_object={
    "object_type": "feed",
    "content": {
        "title": "오늘의 디저트",
        "description": "아메리카노, 빵, 케익",
        "image_url": "https://mud-kage.kakao.com/dn/NTmhS/btqfEUdFAUf/FjKzkZsnoeE4o19klTOVI1/openlink_640x640s.jpg",
        "image_width": 640,
        "image_height": 640,
        "link": {
        "web_url": "http://www.daum.net",
        "mobile_web_url": "http://m.daum.net",
        "android_execution_params": "contentId=100",
        "ios_execution_params": "contentId=100"
        }
    },
    "item_content": {
        "profile_text": "Kakao",
        "profile_image_url": "https://mud-kage.kakao.com/dn/Q2iNx/btqgeRgV54P/VLdBs9cvyn8BJXB3o7N8UK/kakaolink40_original.png",
        "title_image_url": "https://mud-kage.kakao.com/dn/Q2iNx/btqgeRgV54P/VLdBs9cvyn8BJXB3o7N8UK/kakaolink40_original.png",
        "title_image_text": "Cheese cake",
        "title_image_category": "Cake",
        "items": [
        { "item": "Cake1", "item_op": "1000원" },
        { "item": "Cake2", "item_op": "2000원" },
        { "item": "Cake3", "item_op": "3000원" },
        { "item": "Cake4", "item_op": "4000원" },
        { "item": "Cake5", "item_op": "5000원" }
        ],
        "sum": "Total",
        "sum_op": "15000원"
    },
    "social": {
        "like_count": 100,
        "comment_count": 200,
        "shared_count": 300,
        "view_count": 400,
        "subscriber_count": 500
    },
    "buttons": [
        {
        "title": "웹으로 이동",
        "link": {
            "web_url": "http://www.daum.net",
            "mobile_web_url": "http://m.daum.net"
        }
        },
        {
        "title": "앱으로 이동",
        "link": {
            "android_execution_params": "contentId=100",
            "ios_execution_params": "contentId=100"
        }
        }
    ]
    }

    template_string = json.dumps(template_object, ensure_ascii=False)
    template_string = "template_object="+template_string
    response = requests.post(url=url, headers=headers, data=template_string)
    print(response.status_code)
    print(response.text)

    return email + nickname



if __name__ == "__main__":
    app.run(debug=True)
