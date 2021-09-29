import time
import requests
import json
from common import utils,read_config,logger



env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["api-admin-transaction_host"]
token=read_config.read_environment()[env]["admin_token"]
headers = {
    "Cookie":token,
    'Content-Type': 'application/json'
}

class ProductAdmin():


    def get_product_onsale(self):
        url=host+"/spu/product/onsales?state=3&page=1&limit=10"
        response=requests.request("get",url,headers=headers,verify=False)

        logger.Logger.debug("请求的url: "+str(url))
        logger.Logger.debug("请求的header"+str(headers))
        logger.Logger.debug("请求返回的状态码"+str(response.status_code))

        return response.json()


    def creat_product(self):
        url = host+"/spu/product"
        data= utils.read_yaml("api-admin-transaction/product.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        logger.Logger.debug(response.request.body)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug(response.json())

        return response.json()

    def product_onsale(self,SpuNumer):
        data="{}"
        url=host+"/spu/product/"+SpuNumer+"/review"
        response=requests.request("PATCH",url,headers=headers,data=data)
        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug(response.json())

        return response.json()


    #商品审核
    def product_spuAudit(self,SpuNumer):
        url="https://dev-platform-test-tool.codemao.cn/api/spu/product/"+SpuNumer+"/audit/manual?auditPass=true"
        headers = {
            'Accept': 'application/json',
            "Cookie": token,
            'Target-URL': 'http://172.16.99.132:5000',
        }

        response=requests.request("POST",url,headers=headers)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))

        return response.text





if __name__ == "__main__":
    pass

    # ProductAdmin=ProductAdmin()
    # SpuNumer=ProductAdmin.creat_product()["data"]
    # ProductAdmin.product_onsale(SpuNumer)
    # time.sleep(10)
    # ProductAdmin.product_spuAudit(SpuNumer)





