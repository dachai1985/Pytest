import os
from Pytest_API.common import Base
import pytest

from Pytest_API.config import Conf
if __name__ == '__main__':
    # 构造测试用例的路径
    report_path = Conf.get_report_path() + os.sep + "result"
    # 构造 HTML 报告的路径
    html_path = Conf.get_report_path() + os.sep + "html"
    # 运行测试用例
    pytest.main(["-s","--alluredir", report_path])
    Base.allure_report(report_path, html_path)

