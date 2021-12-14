import yaml
import time
import os
from common import read_config

basic_path=os.path.dirname(os.path.dirname(__file__))

"返回当前时间戳"
def get_timestamp():
    return int(time.time())

"读取测试数据"
def read_yaml(filename):
    file = os.path.join(basic_path, "data", filename)
    return yaml.safe_load(open(file=file))

"获取配置的默认host环境"
def get_dafalut_environment():
    return read_config.read_environment()["dafalut"]


def product_title(data=read_yaml("product.yaml")):
    gradecode = []
    for grade in data["grade"]:
        gradecode.append(grade["grade_code"])
    sectioncode = []
    for section in data["section"]:
        sectioncode.append(section["section_code"])
    category = data["category_name"]
    lesson_project = data["lesson_project"]
    data["title"] = gradecode[0][-1] + "年级" + lesson_project + category + sectioncode[0][-1] + "阶段"
    return data["title"]

def businessType_to_business(businessType):
    businesses={
        1:"小火箭",
        2:"探月",
        3:"小火箭b2C",
        4:"探月B2C",
        5:"幼儿园",
        6:"定制课",
        7:"深空b2C",
        8:"小火箭B2C公开课",
        9:"探月B2C",
        10:"口袋派",
        11:"芒果课堂",
        12:"用户平台部",
        13:"新火箭",
        14:"编测"
    }
    return businesses.get(businessType,None)

def attribute_to_form(attribute):
    forms={
        1:"体验课",
        2:"正式课",
        3:"拓展课",
        5:"轻课"
    }
    return forms.get(attribute,None)


def platformid_to_platform(platform):
    platforms={
        1:"IDE",
        5:"BOX2",
        8:"NEMO",
        9:"KIDS",
        15:"PYTHON",
    }
    return platforms.get(platform,None)

def packge_name(data=read_yaml("package.yaml")):
    businessType = data["businessType"]
    attribute = data["attribute"]
    platform=data["platform"]

    businessType=businessType_to_business(businessType)
    attribute=attribute_to_form(attribute)
    platform = platformid_to_platform(platform)
    data["name"]=businessType+attribute+"_"+platform
    return data["name"]


if __name__ == "__main__":
    print(packge_name())



















