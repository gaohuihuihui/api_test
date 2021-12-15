import pytest
import allure
from common import logger
import baseapi.tiger_api
from baseapi import codemao_app_api,tiger_api

TigerApi=baseapi.tiger_api.TigerApi()
CodemaoappApi=codemao_app_api.CodemaoappApi()



@pytest.fixture(scope='session')
def login():
    userId = TigerApi.web_login(username='15235957716', password='codemao666').json()['user_info']['id']
    logger.Logger.info("userid:  " + str(userId))
    yield userId
@allure.title("验证b2c用户的usercode")
def test_usercode_b2c(login):
    userId=login
    result = CodemaoappApi.userCodeV2(userId)
    assert result.status_code == 200
    # assert '小火箭体验课' in result.json()['courseFormNames']


@allure.title("验证非b2c用户登陆")
def test_usercode_notb2c():
    pass



