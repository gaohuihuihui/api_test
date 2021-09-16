import yaml
import time

class Utils():

    #加上文件打开异常处理
    @classmethod
    def read_environment(self):
        return yaml.safe_load(open("/Users/a1234/github/api_test/enviorment.yaml"))

    #获取当前时间戳
    @classmethod
    def udid(self):
        return str(time.time()).replace(".", "")[0:10]











