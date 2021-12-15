import pytest
from  baseapi import tiger_api


TigerApi=tiger_api.TigerApi()

@pytest.fixture(scope='session')

def token():
    loginresult=TigerApi.web_login(username='15521242762',password='a123456')
    token=loginresult.json()['auth']
    userId=loginresult.json()['user_info']['id']
    yield token,userId




