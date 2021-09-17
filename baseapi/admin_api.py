import requests
import json
from common import utils


'''
设置接口的一些公共属性
'''
admin_token = utils.Utils.read_environment()["admin_token"]
host = "https://test-codecamp-teaching-system.codemao.cn"
headers = {"Cookie": admin_token}


class Admin():
    '''
    创建新的课程
    :param:neme 课程名称
    :param:previewUrl 课程预览图片
    :param:editorType 编辑器类型（1：nemo 2 python）
    :param:classType 课程内容类型 (1:编程课)
    :param:description 课程描述
    '''
    def creat_newcourse(self,name="自动化创新课",
                        previewUrl="https://dev-cdn-common.codemao.cn/dev/607/16316767178381.png",
                        editorType=1,
                        classType=1,

                        description="自动化"):

        return requests.post(url=host+"/ty-courses/base",
                      json={
                          "name":name,
                          "previewUrl":previewUrl,
                          "editorType":editorType,
                          "classType":classType,
                          "description":description
                      },headers=headers)

    '''
    查看课程列表 
    '''
    def course_list(self,**kwargs):
        return requests.get(url="https://test-codecamp-admin.codemao.cn/admin/v2/courses?page=1&limit=10",
                            params={
                                "page":1,
                                "limit":10
                            },headers=headers
                            )





