# -*- coding: utf-8 -*-
import requests
import json
import cv2
import numpy as np
from datetime import datetime
import config

SPOON = 1
NO_SPOON = 2

print("결제하시겠습니까?")
input()
print("결제되었습니다.")

print("================= 가상 데이터 ===============")

demo_data = {
    'receiptID': 'PPQRECEIPT',
    'sellerPhone': '01033507347',
    'destinationAddr1': '경상북도 구미시 거의동 대학로 61',
    'destinationPhoneNum': '01012341234',
    'shopRequest': '항상 응원합니다.',
    'deliveryRequests': '조심히 와주세용',
    'orderDate': str(datetime.now()),
    'spoon': SPOON,
    'origin': '쌀(국내산), 돼지고기(미국산), 고춧가루(중국산)',
    'menus': [
        {
            'menuName': '돼지국밥',
            'quantity': 1,
            'price': '7000'
        },
        {
            'menuName': '순대국밥',
            'quantity': 2,
            'price': '7500'
        }
    ]
}

print("결제일:", demo_data['orderDate'], " 가게: 금오공대국밥")
for data in demo_data["menus"]:
    print(data["menuName"], data["price"],
          data["quantity"], int(data["price"])*data["quantity"])

print("===========================================")

headers = {'Content-Type': 'application/json'}
res = requests.post(config.RECEIPT_HOST+'receipts',data=json.dumps(demo_data), headers=headers)
if res.status_code == 200:
    result = res.json()
    res = requests.post(config.QR_HOST+'qr/',data=json.dumps(result))
    result = res.json()
    image_nparray = np.asarray(bytearray(requests.get(config.QR_HOST+f"qr/{result['path']}").content), dtype=np.uint8)
    image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    cv2.imshow('QR', image)
    cv2.waitKey(0)
else:
    print("QR 생성 실패")
print("감사합니다")
input("아무키나 눌러주세요...")
