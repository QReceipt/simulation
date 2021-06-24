import requests
import json
import cv2
import numpy as np

print("결제하시겠습니까?")
input()
print("결제되었습니다.")

print("=================가상 데이터===============")

user = {
    "email":ID,
    "password":PASSWORD
}

login_res = requests.post('http://mmyu.synology.me:8080/user/login', data=json.dumps(user))


headers = {'Authorization': 'Bearer '+login_res.json()["access_token"]}

demo_data = {
  "orderDate": "21/06/20",
  "orderID": 1472583691,
  "seller": "주단태",
  "sellerEmail": "sellerEmail@example.co.kr",
  "sellerHP": "010-0000-0000",
  "orderItem": [
    {
      "menuId": 1,
      "menuName": "생수",
      "quantity": 4,
      "price": 4000
    },
    {
      "menuId": 2,
      "menuName": "주단태빌리지 피규어",
      "quantity": 1,
      "price": 150000
    }
  ]
}


print(f"결제일: {demo_data['orderDate']}  점주: {demo_data['seller']}")
for i in demo_data["orderItem"]:
    print(i["menuName"], i["price"], i["quantity"], i["price"]*i["quantity"])
 

print("===========================================")

# res = requests.post('http://mmyu.synology.me:8080/receipt', data=json.dumps(demo_data),headers=headers)

url = 'https://ebook.nowon.kr/file/pfile/skin/qrcode_20181214220149.png'

# os.system("curl " + url + " > qr.jpg")


# imgFile = "qr.jpg" 
# img = cv2.imread(imgFile, cv2.IMREAD_COLOR) 
# cv2.imshow('QR', img) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows()
image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
cv2.imshow('QR', image)
cv2.waitKey(0)

print("감사합니다")
