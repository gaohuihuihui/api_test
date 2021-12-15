import requests
from common import read_config
from baseapi import client




class CodemaoappApi(client.HttpClient):
    def __init__(self):
        super(CodemaoappApi, self).__init__()
        self.host=read_config.read_environment()[self.env]["codemao_app_web_host"]

    def index_product_V1(self):
        url=self.host+"/index/product"
        response=requests.request("GET",url,headers=self.headers)
        return response

    def index_product_V2(self):
        url = self.host + "/index/product/module"
        response = requests.request("GET", url, headers=self.headers)
        return response

    def userCodeV2(self,userId):
        url = self.host + "/user/userCodeV2"
        param={'userId':userId}
        response = requests.request("GET", url, headers=self.headers,params=param)
        return response


if __name__=="__main__":
    CodemaoappApi=CodemaoappApi()
    print(CodemaoappApi.host)
    res=CodemaoappApi.userCodeV2("4630091")
    print(res.request.url)
    print(CodemaoappApi.userCodeV2("4630091").json())



