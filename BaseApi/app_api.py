
import requests

host= "https://test-gateway.codemao.cn/codemao-app-web"


class App():
    def get_usercodev2(self):
        token = ""
        headers = {
            'Authorization': token
        }
        return requests.get(url=host+"/user/userCodeV2",
                     headers=headers)

    def get_usercodev22(self, userId):

        return requests.get(url=host + "/user/userCodeV2",
                     params={"userId": userId},)
