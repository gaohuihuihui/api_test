import baseapi.codecamp_marketing.package_admin
from baseapi.api_tiger import account
from baseapi.api_admin_transaction import *
from baseapi import *

import requests

url = "https://test-api-admin-transaction.codemao.cn/products/sku/price?page=1&limit=10"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
  'Origin': 'https://test-transaction-admin.codemao.cn',
  'Connection': 'keep-alive',
  'Referer': 'https://test-transaction-admin.codemao.cn/',
  'Cookie': '__ca_uid_key__=2ec8d972-5ac5-4368-8d51-a359922a1fc6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221474512687%22%2C%22first_id%22%3A%2217c16a70c1a8-09d450a0b18cad8-455f6c-1296000-17c16a70c1b1d2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22bcmapp%22%2C%22%24latest_utm_content%22%3A%22qingke%22%2C%22%24latest_utm_term%22%3A%22homecard%22%7D%2C%22%24device_id%22%3A%2217c16a70c1a8-09d450a0b18cad8-455f6c-1296000-17c16a70c1b1d2%22%7D; staging_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IuiBguS6mui_kCIsImVuaWQiOjMwNzgsImlhdCI6MTYzMjkzMDY1NywianRpIjoiZjQxOWQ1MGQtN2Q0NS00NDIyLWIyNjctYjNlZTk5NDYwZGMzIn0.HO9_vyhKY3bdAxG5oYRVmw-Gltbr-yieH5R3lEY0_nk; staging-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjYyMDIsImlhdCI6MTYzMjkwMTg1NywianRpIjoiMDk5NjI4NGYtMjEzZC0xMWVjLTlhOTYtZGY2MTg2YmYxYmEwIn0.fLdQFK12NhRK36I0h94dt3YACqROndj5OGLGBu10HSw; internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumrmOmjnue6oiIsImVuaWQiOjQ2MTgsImlhdCI6MTYzMjczMTIyNSwianRpIjoiYTAxNWNmNmMtNGNmNC00MWQyLTkxMWEtZjE4NjNjODg3MDYzIn0.YFoKsKWZwl1agrYCXYZ5b1aa110MKF--qK0Q5N8F2ho; admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjQzNTYsImlhdCI6MTYzMjcwMjQyNSwianRpIjoiYjI4NjU2NTQtMWY2Yy0xMWVjLWE4NGYtMjUzOTczYzk0YzNjIn0.XKAq75qOK39I6Ze1Tf3EF4fYsBUOd7mXdQhU3JVhk3Y; test-authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxMDAwMTAyODEyLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiI2NWVkQ1R5ZyIsImV4cCI6MTYzNjgxNTU5MywiaWF0IjoxNjMyOTI3NTkzLCJqdGkiOiI0MTJlYWM0MS0yMjhiLTQ0ZGUtODI2Yi02OWEyYTZjYmVkNzEifQ.7xmJFhUl3K_5v-JCcFdxAgiK4-fTJyC4zB01JwwlBO0; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IuiBguS6mui_kCIsImVuaWQiOjEwNSwiaWF0IjoxNjMzNjc2NzE1LCJqdGkiOiI2OGY0Y2JjZi0yYjM0LTQyM2QtODg4ZS00YTUyN2IwNDNlYWUifQ.910JFpyeOjc6396qqzKntlaMmsPpc-mOdkkhBn9-g0I; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg3ODQsImlhdCI6MTYzMzY0NzkxNSwianRpIjoiMTY3YjMyNDktMjgwNi0xMWVjLTk2MjYtMWY4NTRkNzFmMGViIn0.QilwI3MS22BHsM8Yw8_FxrS8kSWphvtwAwoidX3noA0',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'TE': 'trailers'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)




