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


class ProductAdmin(object):


    def get_product_onsale(self):
        url=host+"/spu/product/onsales?state=3&page=1&limit=10"
        response=requests.request("get",url,headers=headers,verify=False)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response


    def creat_product(self):
        url = host+"/spu/product"
        data= utils.read_yaml("api-admin-transaction/product.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        spuNumer=response.json()["data"]

        logger.Logger.debug(response.request.body)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return (response,spuNumer)

    def product_onsale(self,SpuNumer):
        data="{}"
        url=host+"/spu/product/"+SpuNumer+"/review"
        response=requests.request("PATCH",url,headers=headers,data=data)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response


    #商品审核
    def product_spuAudit(self,SpuNumer):

        if env=="test":
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
            # logger.Logger.debug("返回的内容如下:" + str(response.json()))
            return response
        else:
            print("只能在测试环境对商品进行审核上架")

    def product_notsale(self):
        pass













if __name__ == "__main__":
        '''
        自动创建商品并且提交审核后上架（仅在测试环境中使用）
        '''
        # productadmin = ProductAdmin()
        # #step:创建一个商品
        # spuNumer = productadmin.creat_product()[1]
        # time.sleep(3)
        # #提交商品审核
        # productadmin.product_onsale(spuNumer)
        # time.sleep(3)
        # #商品上架
        # productadmin.product_spuAudit(spuNumer)
        #








