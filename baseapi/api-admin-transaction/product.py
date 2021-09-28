import requests
import json

from common import utils


class Product():
  def creat_product(self):
    url = "https://test-api-admin-transaction.codemao.cn/spu/product"
    data= utils.read_yaml("product.yaml")
    headers = {
      'Cookie':"__ca_uid_key__=2ec8d972-5ac5-4368-8d51-a359922a1fc6; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IuiBguS6mui_kCIsImVuaWQiOjEwNSwiaWF0IjoxNjMyMjgxNTA0LCJqdGkiOiI4MWUwNjU5OS0yMjJhLTQzMTYtYjMxYy0zMzVlYTM2YzM5ZjEifQ.QvxjM388BVYq8_vHqlp_FONLdB_mT-eob08_a--8Xk0; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg3ODQsImlhdCI6MTYzMjI1MjcwNCwianRpIjoiOWJjNzFiNTEtMWI1NS0xMWVjLThiYmQtNmQ1ODU2YmFhNTBiIn0.Pdomf8ciyjFp553S8tO3NBGNK1fMIQUwxPFpj3gfF3o",
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    return response.json()




if __name__ == "__main__":
  pass
