import requests
import json
from Utils import utils


'''
设置接口的一些公共属性
'''
admin_token = utils.Utils.read_environment()["admin_token"]
host = "https://test-codecamp-teaching-system.codemao.cn"
headers = {"authorization": admin_token}


class Package():

    '''
    创建新的课程
    :param:课程名称
    :param：
    :param：

    '''
    def creat_newcourse(self,name="自动化创新课",
                        previewUrl="https://dev-cdn-common.codemao.cn/dev/607/16316767178381.png",
                        editorType=1,
                        classType=1,

                        description="自动化",**kwargs):

        return requests.post(url=host+"/ty-courses/base",
                      json={
                          "name":name,
                          "previewUrl":previewUrl,
                          "editorType":editorType,
                          "classType":classType,
                          "description":description
                      },headers=headers)

    #查看课程列表
    def course_list(self,**kwargs):
        return requests.get(url="https://test-codecamp-admin.codemao.cn/admin/v2/courses?page=1&limit=10",
                            params={
                                "page":1,
                                "limit":10
                            },headers=headers
                            )



if __name__=="__main__":
    Package().creat_newcourse()
    print(Package().course_list().status_code)
    print(Package().course_list().request.headers)
    print(Package().course_list().json())


