# from common import Base
# from config import Conf
# import os
from testcase.test_api_excel import TestExcelCase
import allure

# def pytest_sessionfinish(session, exitstatus):
#     # 使用 getoption 方法获取 alluredir 的值
#     report_path = Conf.get_report_path() + os.sep + "result"
#     # 构造 HTML 报告的路径
#     html_path = Conf.get_report_path() + os.sep + "html"
#
#     print("测试报告路径：", report_path)
#     print("测试报告HTML路径：", html_path)

    # Base.allure_report(report_path, html_path)
    # Base.send_email(subject="Test API Report", content="Test is Done，Please check the report！", files=[report_path + os.sep + "report.html"])