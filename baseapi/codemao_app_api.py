import json
import requests
from common import read_config,utils
import jsonpath


env=read_config.read_environment()["defalut"]

codemao_app_web_host=read_config.read_environment()[env]["codemao_app-web_host"]

headers = {
    'Content-Type': 'application/json'}


