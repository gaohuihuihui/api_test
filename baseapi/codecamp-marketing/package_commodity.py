import requests
import json

import utils


def package_commodity(packageId):
    url = "https://test-codecamp-marketing.codemao.cn/packages/"+str(packageId)+"/commodity"
    data= utils.read_yaml("package_commodity.yaml")
    headers = {
        'Cookie':"__ca_uid_key__=2ec8d972-5ac5-4368-8d51-a359922a1fc6; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IuiBguS6mui_kCIsImVuaWQiOjEwNSwiaWF0IjoxNjMyNDU0MDcxLCJqdGkiOiI1ZDAyMTY2Ny04ZTdjLTRjZTUtYWU0NS00OGYyMjg3MDljMTAifQ.umN3vW7v7wujs8zSvrsC7DGJjHmFr0Fsh-HPLXn_0Lw; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg3ODQsImlhdCI6MTYzMjQyNTI3MSwianRpIjoiNjYyN2NjNzUtMWNlNy0xMWVjLThiY…rm%22%3A%22homecard%22%7D%2C%22%24device_id%22%3A%2217c16a70c1a8-09d450a0b18cad8-455f6c-1296000-17c16a70c1b1d2%22%7D; sajssdk_2015_cross_new_user=1; test-authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxNDc0NTEyNjg3LCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiI5Q1l0Z3oxMCIsImV4cCI6MTYzNjM1NTY5MywiaWF0IjoxNjMyNDY3NjkzLCJqdGkiOiJjOTVjODJhMC05ZDVkLTRkOWItOGIzNy1lMDEzODg5ZDY4ZmQifQ.e7QizCLVK4gvB4NiTabFIuIse6hqhN8VZuZUQUbFgS0",
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.request.url)
    print(response.request.body)
    print(response.request.headers)

    return response.json()

if __name__ == "__main__":
    print(package_commodity(3434))
