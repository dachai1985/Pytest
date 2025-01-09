import pytest


class TestDemo:
    # data_list = ["test1","test2"]
    data_list = [("test1","123456"),("test2","1234567")]

    # 数据参数化
    # @pytest.mark.parametrize("name", data_list)
    @pytest.mark.parametrize(("name","passwd"), data_list)
    def test_a(self, name, passwd):
        print("test_a")
        print(name, passwd)
        assert 1

    @pytest.mark.parametrize('pwd', [33, None, 44, 55])
    @pytest.mark.parametrize('name', [11, 22, ])
    def test_add1(self, name, pwd):
        print(f'name:{name} pwd:{pwd}')

    data1 = [
        [1, 1, 2],
        [2, 2, 4],
        [3, 3, 6],
        [4, 4, 8]
    ]
    @pytest.mark.parametrize("a,b,c", data1)
    def test_b(self, a, b, c):
        print(f"\na,b,c is: {a},{b},{c}")


    data2 = [{"user": "admin", "password": "123456"},
            {"user": "super", "password": "654321"},
            {"user": "sysadmin", "password": "321456"}
            ]
    @pytest.mark.parametrize("test_data", data2)
    def test_c(self,test_data):
        print(f"username is {test_data['user']}\n password is {test_data['password']}")

    @pytest.mark.parametrize("input,expected", [pytest.param(2, 4, id="case1"),
                                                pytest.param(3, 9, id="case2"),
                                                pytest.param(5, 25, id="case3")])
    def test_multiply(self, input, expected):
        assert input * input == expected

    @pytest.mark.parametrize("input,expected", [pytest.param(2, 4, id="case1"),
                                                pytest.param(3, 10, id="case2", marks=pytest.mark.xfail),
                                                pytest.param(5, 25, id="case3", marks=pytest.mark.skip)])
    def test_multiply2(self, input, expected):
        assert input * input == expected

if __name__=="__main__":
    pytest.main([__file__])