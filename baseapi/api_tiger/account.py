import json
import time

import requests
from common import utils,read_config,logger

env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["account_api_host"]
token=read_config.read_environment()[env]["app_token"]

user=read_config.read_user()[env]

headers = {
    'Content-Type': 'application/json'
}


class Account(object):


    def app_login(self,username=user["app"]["username"],password=user["app"]["password"]):
        url = host + "/tiger/v3/app/accounts/login"
        data={"identity":username,
              "password":password,
              "pid":"BChYw2XR"}

        response=requests.request("POST",url,data=json.dumps(data),headers=headers)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        print(response.request.body)

        return response


    def admin_login(self):
        pass



    def app_logout(self,token):
        url=host+"/tiger/v3/app/accounts/logout"
        headers = {
            'Content-Type': 'application/json',
            'Authorization':token
        }
        response=requests.request("POST",url,headers=headers)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug(response.text)
        # logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response.status_code



if __name__=="__main__":


    account=Account()
    result=account.app_login()
    token=result.cookies.values()[0]
    print(token)



    # print(json.dumps(account.app_login())["auth"])
    # print(json.dumps(account.app_login()))









