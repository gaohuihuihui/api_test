import json
import requests
from common import read_config,utils
import jsonpath
from baseapi import client


class TransactionApi(client.HttpClient):
    def __init__(self):
        super(TransactionApi, self).__init__()
        self.host=read_config.read_environment()[self.env]["api_admin_transaction_host"]

    def get_product_onsale(self):
        url=self.host+"/spu/product/onsales?state=3&page=1&limit=10"
        response=requests.request("get",url,headers=self.headers,verify=False)

        return response


    def creat_product(self):
        url = self.host+"/spu/product"
        data= utils.read_yaml("api_admin_transaction/product.yaml")
        # data["title"]=utils.product_title(data)
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))
        spuNumer=response.json()["data"]



        return (response,spuNumer)

    def product_onsale(self,spuNumer):
        data="{}"
        url=self.host+"/spu/product/"+spuNumer+"/review"
        response=requests.request("PATCH",url,headers=self.headers,data=data)



        return response


    # 商品审核
    # def product_spuAudit(self,spuNumer):
    #
    #     if self.env=="test":
    #         url="https://dev-platform-test-tool.codemao.cn/api/spu/product/"+spuNumer+"/audit/manual?auditPass=true"
    #         headers = {
    #             'Accept': 'application/json',
    #             "Cookie": token,
    #             'Target-URL': 'http://172.16.99.132:5000',
    #         }
    #
    #         response=requests.request("POST",url,headers=headers)
    #         return response
    #     else:
    #         print("只能在测试环境对商品进行审核上架")

    def product_notsale(self,spuNumer):


        url=self.host+"/spu/product/"+spuNumer+"/offsale"
        data={"offsaleTime":utils.get_timestamp()}

        response = requests.request("PATCH", url, headers=self.headers, data=json.dumps(data))

        return response

    def delete_product(self,spuNumer):
        url=self.host+"/spu/product/"+spuNumer
        response = requests.request("DELETE", url, headers=self.headers)

        return response



if __name__=="__main__":
    TransactionApi=TransactionApi()
    print(TransactionApi.host)




