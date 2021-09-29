import requests
import json
from common import utils,read_config

env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["codecamp-marketing_host"]
token=read_config.read_environment()[env]["admin_token"]
headers = {
    "Cookie": token,
    'Content-Type': 'application/json'
}

class TermAdmin():


    def creat_terms(packageId):

        url = "https://test-codecamp-marketing.codemao.cn/terms"
        data = utils.read_yaml("codecamp-marketing/terms.yaml")
        data["packageId"]=packageId

        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        print(response.request.body)
        print(response.status_code)

        return response.json()

if __name__ == "__main__":
    pass



