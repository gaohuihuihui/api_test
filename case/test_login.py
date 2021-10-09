from baseapi.api_tiger import account
from common import utils,read_config

env=utils.get_dafalut_environment()
user=read_config.read_user()[env]["app"]
account_api=account.Account()


class TestLogin(object):
    def test_case1(self):
        assert account_api.app_login(username=user["username"],password=user["password"]).status_code==200




