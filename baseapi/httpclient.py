from common import  read_config
from common import utils

env=utils.get_dafalut_environment()
admin_token=read_config.read_environment()[env]["admin_token"]


class HttpClient():
    def  __init__(self):
        self.headers= {'Cookie': admin_token,
                       'Content-Type': 'application/json'}

