import pytest
from baseapi.api_tiger import account


class TestLogin():

    def __init__(self):
        self.account_api=account.Account()

    def test_case1(self):
        assert  self.account_api.app_login().status_code==200





