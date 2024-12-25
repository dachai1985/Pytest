import os
from utils.YamlUtil import YamlReader
# 获取项目基本目录
# 当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"
# 定义config目录的路径
_data_path = BASE_DIR + os.sep + "data"
# 定义conf.yml文件的路径
_config_file = _config_path + os.sep + "conf.yml"
# 定义db.yml文件的路径
_db_config_file = _config_path + os.sep + "db_conf.yml"
# 定义config目录的路径
_report_path = BASE_DIR + os.sep + "report"
# 定义log文件的路径
_log_path = BASE_DIR + os.sep + "logs"

# 获取report绝对路径
def get_report_path():
    return _report_path

def get_data_path():
    return _data_path

def get_db_config_file():
    return _db_config_file

def get_config_path():
    return  _config_path

def get_config_file():
    return  _config_file

def get_log_path():
    return  _log_path

# 读取配置文件
class ConfigYaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()
    # 定义方法获取需要信息
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    # 获取测试用例文件
    def get_excel_file(self):
        return self.config["BASE"]["test"]["case_file"]

    # 获取测试用例sheet名称
    def get_excel_sheet_name(self):
        return self.config["BASE"]["test"]["case_sheet"]

    # 获取日志级别
    def get_conf_log(self):
        return self.config["BASE"]["log_level"]
    # 获取文件扩展名
    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]

    # 获取数据库连接信息
    def get_db_conf_info(self, db_alias):
        return self.db_config[db_alias]

    # 获取Email信息
    def get_email_info(self):
        return self.config["Email"]

if __name__ == "__main__":
    conf_read = ConfigYaml()
#   print(conf_read.get_conf_url())
#   print(conf_read.get_conf_log())
#   print(conf_read.get_conf_log_extension())
#   print(conf_read.get_db_conf_info("db_awesome"))
#   print(conf_read.get_excel_file())
#   print(conf_read.get_excel_sheet_name())
    print(conf_read.get_email_info())

