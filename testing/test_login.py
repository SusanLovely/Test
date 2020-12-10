import pytest


def test_case1():
    print(f"case1=")


def test_case2():
    print("case2")


@pytest.mark.parametrize("login", [
    ('username', 'password'),
    ('username1', 'password1')
], indirect=True)
def test_case3(login):
    print(f"{login[0]}")
