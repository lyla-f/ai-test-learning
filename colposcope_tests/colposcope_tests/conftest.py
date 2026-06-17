# conftest.py - 全局配置和fixture
# 阴道镜系统接口自动化测试
import pytest
import requests
import warnings
warnings.filterwarnings("ignore")

BASE_URL = "https://127.0.0.1:7002"
ADMIN_USER = "admin"
ADMIN_PASS = "FsKgVFHIqn5oc2J2eqaxjg=="  # AES加密后的密码


def get_token():
    """获取登录token"""
    res = requests.post(
        f"{BASE_URL}/api/common/login",
        json={"username": ADMIN_USER, "password": ADMIN_PASS},
        verify=False
    )
    data = res.json()
    assert data["code"] == 200, f"登录失败: {data}"
    return data["data"]["accessToken"]


@pytest.fixture(scope="session")
def token():
    """session级别token，整个测试过程只登录一次"""
    return get_token()


@pytest.fixture(scope="session")
def headers(token):
    """带认证的请求头"""
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL
