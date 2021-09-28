import yaml
import time
import os
from common import read_config

basic_path=os.path.dirname(os.path.dirname(__file__))


'''
返回当前时间戳
'''
def get_time():
    return str(time.time()).replace(".", "")[0:10]

def read_yaml(filename):
    file = os.path.join(basic_path, "data", filename)
    return yaml.safe_load(open(file=file))

def get_date():
    return time.time()

"获取配置的默认host环境"
def get_dafalut_environment():
    return read_config.read_environment()["dafalut"]

def get_app_token():

    pass
def get_admin_token():
    pass


if __name__=="__main__":
    print(get_dafalut_environment())

















