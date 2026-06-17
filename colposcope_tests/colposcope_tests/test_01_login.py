# test_01_login.py - 登录模块接口测试
import requests
import warnings
warnings.filterwarnings("ignore")

BASE_URL = "https://127.0.0.1:7002"
URL = f"{BASE_URL}/api/common/login"
CORRECT_PASS = "FsKgVFHIqn5oc2J2eqaxjg=="


def login(username, password):
    return requests.post(URL, json={"username": username, "password": password}, verify=False)


# ============ 正常登录 ============

def test_login_success():
    """正确账号密码登录成功"""
    res = login("admin", CORRECT_PASS)
    data = res.json()
    assert res.status_code == 200
    assert data["code"] == 200
    assert data["msg"] == "OK"
    assert "accessToken" in data["data"]
    assert "expiresIn" in data["data"]
    print(f"✅ 登录成功，token已获取")


def test_login_token_not_empty():
    """登录成功后token不为空"""
    res = login("admin", CORRECT_PASS)
    token = res.json()["data"]["accessToken"]
    assert token and len(token) > 0
    print(f"✅ Token非空，长度: {len(token)}")


def test_login_expires_in():
    """登录成功expiresIn为正数"""
    res = login("admin", CORRECT_PASS)
    expires = res.json()["data"]["expiresIn"]
    assert expires > 0
    print(f"✅ Token有效期: {expires}秒")


# ============ 密码错误 ============

def test_login_wrong_password():
    """错误密码被拦截"""
    res = login("admin", "wrongpassword")
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 错误密码被拦截: {data['msg']}")


def test_login_empty_password():
    """密码为空被拦截"""
    res = login("admin", "")
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 空密码被拦截")


# ============ 账号问题 ============

def test_login_wrong_username():
    """不存在的账号被拦截"""
    res = login("notexist_user_xyz", CORRECT_PASS)
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 不存在账号被拦截: {data['msg']}")


def test_login_empty_username():
    """账号为空被拦截"""
    res = login("", CORRECT_PASS)
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 空账号被拦截")


def test_login_both_empty():
    """账号密码均为空"""
    res = login("", "")
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 账号密码均为空被拦截")


# ============ 安全测试 ============

def test_login_sql_injection():
    """SQL注入不能绕过登录"""
    res = login("' OR 1=1--", "anypassword")
    data = res.json()
    assert data["code"] != 200
    print(f"✅ SQL注入被拦截")


def test_login_response_structure():
    """失败响应结构正确"""
    res = login("admin", "wrongpassword")
    data = res.json()
    assert "code" in data
    assert "msg" in data
    print(f"✅ 失败响应结构正确")
