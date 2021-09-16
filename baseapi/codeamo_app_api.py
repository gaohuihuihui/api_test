
import requests

'''
设置接口的一些公共属性
'''

host= "https://gateway.codemao.cn/codemao-app-web"
token = ""
headers = {
    'Authorization': token
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




