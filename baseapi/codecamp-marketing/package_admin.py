import time

import requests
import json
from common import utils,read_config,logger,mysql

mysql=mysql.Mysql()



env=utils.get_dafalut_environment()
host1=read_config.read_environment()[env]["codecamp-teaching_host"]
host2=read_config.read_environment()[env]["codecamp-marketing_host"]

token=read_config.read_environment()[env]["admin_token"]
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    "Cookie": token,
    'Content-Type': 'application/json;charset=utf-8'

}

class PackageAdmin(object):

    def get_packages(self):
        url=host2+"/packages/list-by-query?page=1&limit=10"
        response=requests.request("GET",url,headers=headers)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        p = response.json()["data"]["items"]

        return (response,p)


    def creat_package(self):

        url = host1+"/packages/base"
        data=utils.read_yaml("codecamp-marketing/package.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:"+ str(response.json()))

        packageId=response.json()["data"]["packageId"]

        return (response,packageId)

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
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response


    def add_chapter_course(self,chapterId):

        url=host1+"/chapters/"+str(chapterId)+"/courses"

        data=utils.read_yaml("codecamp-marketing/chapter_course.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response



    def package_commodity(self,packageId):
        url = host1+"/packages/"+str(packageId)+"/commodity"
        data = utils.read_yaml("codecamp-marketing/package_commodity.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response

    def term_config(self,packageId):
        url = host1+"/packages/"+str(packageId)+"/term-config"
        data = utils.read_yaml("codecamp-marketing/term_config.yaml")
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response


if __name__=="__main__":


    logger.Logger.info("*******")
    logger.Logger.info("测试环境是:" +env)
    logger.Logger.info("测试host:"+host1)
    logger.Logger.info("测试host:"+host2)
    logger.Logger.info("token是："+token)
    logger.Logger.info("header是："+str(headers))

    '''
    自动创建课包
    '''

    packageadmin = PackageAdmin()
    packageId=3453
    #step1:创建课包：
    # packageId=packageadmin.creat_package()[1]
    # time.sleep(3)
    #创建课包对应的章节：
    packageadmin.creat_chapter(packageId)
    time.sleep(3)
    #给章节加课程
    mysql.cur.execute("SELECT id from tbl_chapter where package_id=" + str(packageId))
    chapterId = (mysql.cur.fetchone()[0])
    mysql.cur.close()
    packageadmin.add_chapter_course(chapterId)












