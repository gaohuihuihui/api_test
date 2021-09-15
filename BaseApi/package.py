import requests
import json

class Package():
    def creat_newcourse(self):
        host = "https://test-codecamp-teaching-system.codemao.cn/ty-courses/base"
        name = "建课"
        previewUrl = "https://dev-cdn-common.codemao.cn/dev/607/16316767178381.png"
        editorType = 1
        classType = 1
        description = "自动建课"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjc0MzEsImlhdCI6MTYzMTY0NDgzMCwianRpIjoiNGIxZDRjMTEtMTVjZS0xMWVjLThiYmQtNmQ1ODU2YmFhNTBiIn0.5luB1_fhsstHBd5ZNT_8JHagOTevZyLK3ZMUYsG54YM"
        }
        data = json.dumps({"name": name, "previewUrl": previewUrl, "editorType": editorType, "classType": classType,
                               "description": description
                               })
        re=requests.request("POST",headers=headers,url=host,data=data)
        return re.json()



    def creat_package(self):
        pass

    def creat_chapter(self):
        pass

    def creat_chapter_course(self):
        pass


if __name__=="__main__":
    print(Package().creat_newcourse())
