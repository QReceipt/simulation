# -*- coding: utf-8 -*-
import requests
import json
import cv2
import numpy as np
from datetime import datetime

SPOON = 1
NO_SPOON = 2

print("결제하시겠습니까?")
input()
print("결제되었습니다.")

print("================= 가상 데이터 ===============")

demo_data = {
    "receiptID": "PPQRECEIPT",
    "sellerPhone": "01033507347",
    "destinationAddr1": "경상북도 구미시 거의동 대학로 61",
    "destinationPhoneNum": "01012341234",
    "shopRequest": "항상 응원합니다.",
    "deliveryRequests": "조심히 와주세용",
    "orderDate": datetime.now(),
    "spoon": SPOON,
    "origin": "쌀(국내산), 돼지고기(미국산), 고춧가루(중국산)",
    "menu": [
        {
            "menuName": "돼지국밥",
            "quentity": 1,
            "price": "7000"
        },
        {
            "menuName": "순대국밥",
            "quentity": 2,
            "price": "7500"
        }
    ]
}

print("결제일:", demo_data['orderDate'], " 가게: 금오공대국밥")
for date in demo_data["menu"]:
    print(date["menuName"], date["price"],
          date["quantity"], date["price"]*date["quantity"])

print("===========================================")

res = requests.post('http://localhost:8000/receipts',
                    data=json.dumps(demo_data))
print(res)


# image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)
# image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
# cv2.imshow('QR', image)
# cv2.waitKey(0)

print("감사합니다")
input("아무키나 눌러주세요...")
