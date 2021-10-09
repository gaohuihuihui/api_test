import time

import requests
import json
from common import utils,read_config,logger,mysql
from baseapi import httpclient

mysql=mysql.Mysql()



env=utils.get_dafalut_environment()
host1=read_config.read_environment()[env]["codecamp-teaching_host"]
host2=read_config.read_environment()[env]["codecamp-marketing_host"]



class PackageAdmin(httpclient.HttpClient):

    def get_packages(self):
        url=host2+"/packages/list-by-query?page=1&limit=10"
        response=requests.request("GET",url,headers=self.headers)

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        p = response.json()["data"]["items"]

        return (response,p)


    def creat_package(self):

        url = host1+"/packages/base"
        data=utils.read_yaml("codecamp_marketing/package.yaml")

        if data["name"]=="":     #如果课包名称为空，则按照某种规则组装一个package_name
            data["name"]=utils.packge_name(data)
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:"+ str(response.json()))

        packageId=response.json()["data"]["packageId"]

        return (response,packageId)

    '''
    :param:packageId:课包id 
    '''
    def creat_chapter(self,packageId):

        url=host1+"/packages/"+str(packageId)+"/chapters"
        data=utils.read_yaml("codecamp_marketing/chapter.yaml")
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response


    def add_chapter_course(self,chapterId):

        url=host1+"/chapters/"+str(chapterId)+"/courses"

        data=utils.read_yaml("codecamp_marketing/chapter_course.yaml")
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))
        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response



    def package_commodity(self,packageId):
        url = host1+"/packages/"+str(packageId)+"/commodity"
        data = utils.read_yaml("codecamp_marketing/package_commodity.yaml")
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response

    def term_config(self,packageId):
        url = host1+"/packages/"+str(packageId)+"/term-config"
        data = utils.read_yaml("codecamp_marketing/term_config.yaml")
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + str(response.json()))

        return response


if __name__=="__main__":
    packageadmin = PackageAdmin()

    # logger.Logger.info("*******")
    # logger.Logger.info("测试环境是:" +env)
    # logger.Logger.info("测试host:"+host1)
    # logger.Logger.info("测试host:"+host2)
    # logger.Logger.info("token是："+token)
    # logger.Logger.info("header是："+str(headers))

    '''
    自动创建课包
    '''
    #step1:创建课包：
    packageId=packageadmin.creat_package()[1]
    time.sleep(3)
    #创建课包对应的章节：
    packageadmin.creat_chapter(packageId)
    time.sleep(3)
    #给章节加课程
    mysql.cur.execute("SELECT id from tbl_chapter where package_id=" + str(packageId))
    chapterId = (mysql.cur.fetchone()[0])
    mysql.cur.close()
    packageadmin.add_chapter_course(chapterId)

    '''
    创建课包结束
    '''











