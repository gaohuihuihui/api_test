import requests
from common import utils,read_config

env=utils.get_dafalut_environment()
host=read_config.read_environment()[env]["codemao-app-web_host"]
token=read_config.read_environment()[env]["app_token"]