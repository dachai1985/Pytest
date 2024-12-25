import os
from common import Base
import pytest
from config import Conf

if __name__ == '__main__':
    # 构造测试用例的路径
    report_path = Conf.get_report_path() + os.sep + "result"
    # 构造 HTML 报告的路径
    html_path = Conf.get_report_path() + os.sep + "html"
    print("测试报告路径111：", report_path)
    print("HTML 报告路径：", html_path)
    # 运行测试用例
    pytest.main(["-s", "--alluredir", report_path, "--clean-alluredir"])
    Base.allure_report(report_path, html_path)

