import requests
import json
from common import utils,read_config,logger
from baseapi import httpclient

env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["codecamp-marketing_host"]


class TermAdmin(httpclient.HttpClient):

    def creat_terms(self,packageId):

        url = host+"/terms"
        data = utils.read_yaml("codecamp_marketing/terms.yaml")
        data["packageId"]=packageId
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + response.json())

        return response.json()

if __name__ == "__main__":
    print(host)



