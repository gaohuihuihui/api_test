import json
import sys
import requests
from common import read_config,utils
from baseapi import client
sys.path.append("..")


class TigerApi(client.HttpClient):

    def __init__(self):
        super().__init__()
        self.tiger_api_host=read_config.read_environment()[self.env]["account_api_host"]
        self.open_service_host=read_config.read_environment()[self.env]["open_service_host"]

    def get_ticket_v2(self):
        data={
	        "identity": "15521242762",
            "pid":"autotest" }
        res=requests.request(method='post',url=self.open_service_host+"/captcha/rule/v2",data=json.dumps(data),headers=self.headers)
        return res

    def web_login(self,username,password):

        data={"identity": username,
               "password": password,
               "pid":"65edCTyg"}
        res=requests.request(method="post",url=self.tiger_api_host+"/tiger/v3/web/accounts/login",data=json.dumps(data),headers=self.headers)
        return  res



if __name__=="__main__":
    # TigerApi=TigerApi()
    #
    # res=TigerApi.web_login(username='15521242762',password='a123456')
    # re2=TigerApi.get_ticket_v2()
    # ticket=jsonpath.jsonpath(re2.json(),"$.ticket")
    # token=jsonpath.jsonpath(res.json(),"$.auth.token")
    # # cookies=res.cookies
    # print(token)
    # print(ticket)
    print(sys.path)




