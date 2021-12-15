import json
import sys
import requests
from common import read_config,utils,mysql
import time
from baseapi import client

sys.path.append("..")


mysql=mysql.Mysql()

class MarketingApi(client.HttpClient):
    def __init__(self):
        super(MarketingApi, self).__init__()
        self.host1= read_config.read_environment()[self.env]["codecamp_teaching_host"]
        self.host2= read_config.read_environment()[self.env]["codecamp_marketing_host"]

    def get_packages(self):
        url=self.host2+"/packages/list-by-query?page=1&limit=10"
        response=requests.request("GET",url,headers=self.headers)

        p= response.json()["data"]["items"]

        return (response,p)


    def creat_package(self):

        url = self.host1+"/packages/base"
        data=utils.read_yaml("package.yaml")

        # if data["name"]==" ":     #如果课包名称为空，则按照某种规则组装一个package_name
        #     data["name"]=utils.packge_name(data)
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))


        packageId=response.json()["data"]["packageId"]

        return (response,packageId)

    '''
    :param:packageId:课包id 
    '''
    def creat_chapter(self,packageId):

        url=self.host1+"/packages/"+str(packageId)+"/chapters"
        data=utils.read_yaml("codecamp_marketing/chapter.yaml")
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))


        return response


    def add_chapter_course(self,chapterId):

        url=self.host1+"/chapters/"+str(chapterId)+"/courses"

        data=utils.read_yaml("codecamp_marketing/chapter_course.yaml")
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        return response



    def package_commodity(self,packageId):
        url = self.host1+"/packages/"+str(packageId)+"/commodity"
        data = utils.read_yaml("codecamp_marketing/package_commodity.yaml")
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))



        return response

    def term_config(self,packageId):
        url = self.host1+"/packages/"+str(packageId)+"/term-config"
        data = utils.read_yaml("codecamp_marketing/term_config.yaml")
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))


        return response

    def creat_class(self, packageId, termId):
        url = self.host2 + "/classes"
        data = utils.read_yaml("codecamp_marketing/classes.yaml")
        data["packageId"] = packageId
        data["termId"] = termId
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        return response

    '''
        创建新的课程
        :param:neme 课程名称
        :param:previewUrl 课程预览图片
        :param:editorType 编辑器类型（1：nemo 2 python）
        :param:classType 课程内容类型 (1:编程课)
        :param:description 课程描述
        '''

    def creat_newcourse(self, name="自动化创新课",
                        previewUrl="https://dev-cdn-common.codemao.cn/dev/607/16316767178381.png",
                        editorType=1,
                        classType=1,

                        description="自动化"):
        return requests.post(url=host + "/ty-courses/base",
                             json={
                                 "name": name,
                                 "previewUrl": previewUrl,
                                 "editorType": editorType,
                                 "classType": classType,
                                 "description": description
                             }, headers=headers)

    '''
    查看课程列表 
    '''

    def course_list(self, **kwargs):
        return requests.get(url="https://test-codecamp-admin.codemao.cn/admin/v2/courses?page=1&limit=10",
                            params={
                                "page": 1,
                                "limit": 10
                            }, headers=headers
                            )

    def creat_terms(self, packageId):
        url = host + "/terms"
        data = utils.read_yaml("codecamp_marketing/terms.yaml")
        data["packageId"] = packageId
        response = requests.request("POST", url, headers=self.headers, data=json.dumps(data))

        logger.Logger.debug("请求的url: " + str(url))
        logger.Logger.debug("请求的header" + str(self.headers))
        logger.Logger.debug("请求返回的状态码" + str(response.status_code))
        logger.Logger.debug("返回的内容如下:" + response.json())

        return response.json()

if __name__=="__main__":
    MarketingApi=MarketingApi()

    '''
    自动创建课包
    '''
    #step1:创建课包：
    packageId=MarketingApi.creat_package()[1]
    time.sleep(3)
    #创建课包对应的章节：
    MarketingApi.creat_chapter(packageId)
    time.sleep(3)
    #给章节加课程
    mysql.cur.execute("SELECT id from tbl_chapter where package_id=" + str(packageId))
    chapterId = (mysql.cur.fetchone()[0])
    mysql.cur.close()
    MarketingApi.add_chapter_course(chapterId)

    '''
    创建课包结束
    '''