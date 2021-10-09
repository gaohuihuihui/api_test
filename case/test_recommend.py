from baseapi.api_tiger import account
from baseapi.codemao_app_web import index_app
from common import logger


def test_a():
    pass
class TestRecommend(object):
    def __init__(cls):
        cls.account_api=account.Account()
        cls.index=index_app.IndexApp()
        cls.token=cls.account_api.app_login(username="15521242762",password="a123456").cookies.values
        logger.Logger.info(cls.token)
    def test_a(self):
        pass