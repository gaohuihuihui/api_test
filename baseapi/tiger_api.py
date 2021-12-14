import json
import requests
from common import read_config,utils
import jsonpath


env=read_config.read_environment()["defalut"]
tiger_api_host=read_config.read_environment()[env]["account_api_host"]
open_service_host=read_config.read_environment()[env]["open-service_host"]
headers = {
    'Content-Type': 'application/json'}


class TigerApi():

    def get_ticket_v2(self):
        data={
	        "identity": "15521242762",
            "pid":"autotest" }
        res=requests.request(method='post',url=open_service_host+"/captcha/rule/v2",data=json.dumps(data),headers=headers)
        return res

    def web_login(self):

        data={"identity": "15521242762",
               "password": "a123456",
               "pid":"65edCTyg"}
        res=requests.request(method="post",url=tiger_api_host+"/tiger/v3/web/accounts/login",data=json.dumps(data),headers=headers)

        return  res



if __name__=="__main__":
    print(tiger_api_host)
    res=TigerApi().web_login()
    re2=TigerApi().get_ticket_v2()
    ticket=jsonpath.jsonpath(re2.json(),"$.ticket")
    token=jsonpath.jsonpath(res.json(),"$.auth.token")
    # cookies=res.cookies
    print(token)
    print(ticket)
    print(env)
    print(open_service_host)




