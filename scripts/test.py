import baseapi.codecamp_marketing.package_admin
from baseapi.api_tiger import account
from baseapi.api_admin_transaction import *
from baseapi import *


account_api=account.Account()

print(account_api.app_login().cookies.values())

api_transaction=baseapi.codecamp_marketing.package_admin.PackageAdmin()



