import pytest


class TestFunc:
    def setup_method(self):
        print("---setup---")
    def teardown_method(self):
        print("---teardown---")

    def test_a(self):
        print("test a")

    def test_b(self):
        print("test b")

if __name__=="__main__":
    pytest.main(["-s", __file__])