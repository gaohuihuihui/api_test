import os
import yaml

'''
配置文件存放目录
environment.yaml：不同项目在不同环境下的域名
db.yaml:mysql数据库连接相关的配置
redis.yaml:redis连接相关的配置
'''
base_path=os.path.dirname(os.path.dirname(__file__))
environment_path=os.path.join(base_path,"config","environment.yaml")
db_path=os.path.join(base_path,"config","db.yaml")
redis_path=os.path.join(base_path,"config","redis.yaml")

'''
读取绝对路径下yaml配置文件
'''
def read_yaml(file):
    return yaml.safe_load(open(file=file))
'''
读取数据库相关的所有配置
'''
def read_db():
    return yaml.safe_load(open(db_path))

'''
读取环境相关的所有配置
'''
def read_environment():
    return yaml.safe_load(open(environment_path))

'''
读取redis相关的所有配置
'''
def read_redis():
    return yaml.safe_load(open(redis_path))

#
# if __name__=="__main__":
#     # print(read_db())
#     # print(read_environment())
#     # print(read_redis())
#     print(read_yaml(file=environment_path))
