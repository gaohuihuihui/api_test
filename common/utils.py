import yaml
import time

'''
返回当前时间戳
'''
def time():
    return str(time.time()).replace(".", "")[0:10]

def read_yaml(filename):
    file = os.path.join(basic_path, "codecamp-marking", filename)
    return yaml.safe_load(open(file=file))

def get_date():
    return time.time()

def get_admin_token():
    pass














