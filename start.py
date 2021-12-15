import pytest
import os


if __name__=="__main__":

    pytest.main(['-sv','/Users/a1234/github/api_test/case'])
    os.system(r"allure generate --clean allure-results -o allure-report")
    os.system('allure open allure-report')  # 打开报告




