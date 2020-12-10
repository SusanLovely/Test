import pytest


@pytest.fixture()
def login(request):
    return request.param


@pytest.fixture()
def calcomment():
    print("计算开始...")
    yield
    print("计算结束....")
