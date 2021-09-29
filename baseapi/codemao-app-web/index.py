
import requests
from common import utils,read_config

env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["codecamp-marketing_host"]
token=read_config.read_environment()[env]["admin_token"]
headers = {
    "Cookie": token,
    'Content-Type': 'application/json'
}

class CodemaoApp():

    '''
    获取用户usercode
    :param userId 如果请求头不带鉴权，则获取传参userId
    '''
    def get_usercodev2(self,userId=None):

        return requests.get(url=host+"/user/userCodeV2",
                            params=userId,
                     headers=headers)
    '''
    获取首页推荐商品(V1.4版本之前)
    '''
    def get_index_product_v1(self):

        return requests.get(url=host+"/index/product",
        headers=headers
        )
    '''
    获取首页推荐商品（V1.4版本之后）
    '''
    def get_index_product_v2(self):

        return requests.get(url=host+"",
                            headers=headers)

#
# if __name__=="__main__":
#     print(CodemaoApp().get_index_product_v1().json()||||)




