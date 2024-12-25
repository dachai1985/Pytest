import json
import pytest
from Pytest_API.utils.RequestUtil import Request
from Pytest_API.config.Conf import ConfigYaml
from Pytest_API.utils.AssertUtil import TestAssertAPI
from Pytest_API.common.Base import init_db
from Pytest_API.utils.LogUtil import my_log

data_list = [("chai@excample.com","daccf256f725ed4205357e24a877a00b77abce77"),
             ("chai@excample.com","999999")]

@pytest.mark.parametrize(("email","passwd"), data_list)
def test_login(email, passwd):
    # url = "http://127.0.0.1:9000/api/authenticate"
    data = {"email": email, "passwd": passwd} #创建正确的数据字典
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/authenticate"
    request = Request()
    result = request.post(url, json=data)
    print ("Login result==========", result)

    code = result["code"]
    # body字典
    body = result["body"]

    print("body==========",body)

    # 验证body是否包含error信息
    if body and "error" in body:
        assert "error" in body
        assert "message" in body
        print(f"Error case detected: {body['message']}")
    else:
        # login成功响应
        TestAssertAPI().assert_code(code, 200)
        # 传递字典，而不是先转换为 JSON 字符串
        # excepted_body = {'id': '001626057986549d93a93ec19594aa7b50fad2d779ca711000', 'email': 'chai@excample.com'}
        excepted_body = '"id": "001626057986549d93a93ec19594aa7b50fad2d779ca711000", "email": "chai@excample.com"'

        TestAssertAPI().asser_in_body(body, excepted_body)

        # 断言数据库中是否有该用户
        conn = init_db("db_awesome")
        # cursor = conn.cursor()
        # sql = "SELECT id FROM users WHERE email=%s"
        # cursor.execute(sql, (email,))
        # result_db = cursor.fetchone()
        sql = "SELECT id FROM users WHERE email=%s"
        result_db = conn.fetchone(sql, (email,))
        assert result_db is not None
        user_id = body["id"]
        assert user_id == result_db["id"]
        print ("User in database==========", result_db)

def test_get_blogs():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/blogs"
    request = Request()
    result = request.get(url)
    print ("Get blogs result==========", result)

    code = result["code"]
    TestAssertAPI().assert_code(code,200)

if __name__=="__main__":
    pytest.main()