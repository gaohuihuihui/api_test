import requests
import json
from common import utils,read_config,logger

env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["codecamp-marketing_host"]
token=read_config.read_environment()[env]["admin_token"]
headers = {
    "Cookie": token,
    'Content-Type': 'application/json'
}

class ClassAdmin(object):

    def creat_class(self,packageId,termId):
        url = host+"/classes"
        data= utils.read_yaml("codecamp-marketing/classes.yaml")
        data["packageId"]=packageId
        data["termId"]=termId
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))


        return  response.json()


if __name__ == "__main__":
   pass
