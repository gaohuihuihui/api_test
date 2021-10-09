import requests
import json
from common import utils,read_config,logger
from baseapi import httpclient

env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["codecamp-marketing_host"]


class ClassAdmin(httpclient.HttpClient):

    def creat_class(self,packageId,termId):
        url = host+"/classes"
        data= utils.read_yaml("codecamp_marketing/classes.yaml")
        data["packageId"]=packageId
        data["termId"]=termId
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))


        return  response


if __name__ == "__main__":
    classadmin=ClassAdmin()
    classadmin.creat_class(packageId=3458,termId=10486)


