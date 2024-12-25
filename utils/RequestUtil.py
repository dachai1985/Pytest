# 创建封装的request方法
import requests
from Pytest_API.utils.LogUtil import my_log

class Request:
    def __init__(self):
        self.log = my_log("Request")

    # 定义公共方法
    def request_apis(self, url, data=None, json=None, headers=None, cookies=None, method="get"):
        # 发送requests请求
        # global r
        if method == "get":
            self.log.info("发送get请求")
            r = requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method == "post":
            self.log.info("发送post请求")
            r = requests.post(url, data=data, json=json, headers=headers, cookies=cookies)

        # 获取结果相应内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 内容存到字典返回
        res = dict()
        res["code"] = code
        res["body"] = body
        return res

    def get(self, url, **kwargs):
        return self.request_apis(url, method="get", **kwargs)

    def post(self, url, **kwargs):
        return self.request_apis(url, method="post", **kwargs)

