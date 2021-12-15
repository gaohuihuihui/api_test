from baseapi import tiger_api
import pytest
import allure
from common import logger
#
# basic_path=os.path.dirname(os.path.dirname(__file__))
# sys.path.append(basic_path)

TigerApi = tiger_api.TigerApi()

@allure.feature("测试登陆模块")
class TestLogin:


    @pytest.mark.parametrize('username,password',[('15521242762','a123456'),
                                                ('15235957716','codemao666')])
    @allure.title("测试b2c用户和非b2c登陆")
    def test_login(self,username,password):
        login_result=TigerApi.web_login(username=username,password=password)
        logger.Logger.info(login_result.json())

        assert login_result.status_code==200



    @pytest.mark.parametrize('username,password,errcode', [('15521242762', '12333','AC3'),
                                                           ('15521242763', 'qqq','AC3'),
                                                           ('', '1122','A'),
                                                           ('1222', '1131331','AC3'),
                                                        ('', '','A')])
    @allure.title("异常输入测试")
    def test_login_fail(self,username,password,errcode):
        login_result = TigerApi.web_login(username=username, password=password)
        logger.Logger.info(login_result.json())
        assert login_result.json()['error_category']==errcode


# if __name__=="__main__":
#     pytest.main(["-s"])


