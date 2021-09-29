import requests
import json
from common import utils,read_config,logger


env=utils.get_dafalut_environment()
host1=read_config.read_environment()[env]["codecamp-teaching_host"]
host2=read_config.read_environment()[env]["codecamp-marketing_host"]

token=read_config.read_environment()[env]["admin_token"]
headers = {
    "Cookie": token,
    'Content-Type': 'application/json'
}

class PackageAdmin():

    def get_packages(self):
        url=host2+"/packages/list-by-query?page=1&limit=10"
        response=requests.request("GET",url,headers=headers)
        return response.json()


    def creat_package(self):

        url = host1+"/packages/base"
        data=utils.read_yaml("codecamp-marketing/package.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))

        return response.json()

    '''
    :param:packageId:课包id 
    '''
    def creat_chapter(self,packageId):

        url=host1+"/packages/"+str(packageId)+"/chapters"
        data=utils.read_yaml("codecamp-marketing/chapter.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))

        return response.json()

    def package_commodity(packageId):
        url = host1+"/packages/"+str(packageId)+"/commodity"
        data = utils.read_yaml("codecamp-marketing/package_commodity.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger

        return response.json()

    def term_config(packageId):
        url = host1+"/packages/" + str(packageId) + "/term-config"
        data = utils.read_yaml("codecamp-marketing/term_config.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))

        return response.json()


if __name__=="__main__":
    PackageAdmin=PackageAdmin()
    # PackageAdmin.get_packages()
    #PackageAdmin.creat_package(3450)
    PackageAdmin.creat_chapter(3450)





