
import requests
from common import utils,read_config,logger


env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["codemao-app-web_host"]
token=read_config.read_environment()[env]["app_token"]
headers = {
    "Authorization": token,
    'Content-Type': 'application/json'
}

class IndexApp(object):



    def index_product_V1(self):
        url=host+"/index/product"
        response=requests.request("GET",url,headers=headers)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response

    def index_product_V2(self):
        url = host + "/index/product/module"
        response = requests.request("GET", url, headers=headers)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response




if __name__=="__main__":
    appindex=IndexApp()
    assert appindex.index_product_V1().status_code==200
    assert appindex.index_product_V2().status_code==200




