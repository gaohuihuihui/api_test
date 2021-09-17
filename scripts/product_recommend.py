import requests
import json
import logging


logging.basicConfig(level="INFO")
normalCourses={}
formalCourses={}
lightCourses={}




request_url="https://gateway.codemao.cn/codemao-app-web/index/product"

re=requests.get(url="https://gateway.codemao.cn/codemao-app-web/index/product")

print(json.dumps(re.json(), indent=2))

normalCourses=re.json()["normalCourses"]

formalCourses=re.json()["formalCourses"]
lightCourses=re.json()["formalCourses"]




# old_01=file.open(
