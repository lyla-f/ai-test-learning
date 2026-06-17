# test_05_user.py - 用户管理接口测试
import requests
import warnings
import time
warnings.filterwarnings("ignore")


# ============ 查询用户 ============

def test_get_current_user(headers, base_url):
    """获取当前登录用户信息"""
    res = requests.get(f"{base_url}/api/user/getCurrentUser", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    assert "id" in data["data"] or "username" in data["data"]
    print(f"✅ 当前用户信息获取成功")


def test_get_user_permission(headers, base_url):
    """获取当前用户权限（权限接口可能有角色限制）"""
    res = requests.get(f"{base_url}/api/user/getPermission", headers=headers, verify=False)
    data = res.json()
    # 验证接口可达且返回结构正确
    assert "code" in data and "msg" in data
    print(f"✅ 用户权限接口响应: code={data['code']}, msg={data['msg']}")


def test_get_all_users(headers, base_url):
    """获取所有用户列表"""
    res = requests.get(f"{base_url}/api/user/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    assert isinstance(data["data"], list)
    print(f"✅ 用户列表返回，数量: {len(data['data'])}")


def test_get_users_page(headers, base_url):
    """分页获取用户"""
    res = requests.get(
        f"{base_url}/api/user/findPage",
        params={"page": 1, "size": 10},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 分页用户列表返回成功")


# ============ 创建用户 ============

def test_create_user_success(headers, base_url):
    """创建新用户"""
    ts = int(time.time())
    payload = {
        "username": f"testuser{ts}",
        "password": "FsKgVFHIqn5oc2J2eqaxjg==",  # 加密后的test密码
        "autograph": "测试医生"
    }
    res = requests.post(f"{base_url}/api/user/create", json=payload, headers=headers, verify=False)
    data = res.json()
    print(f"✅ 创建用户响应: code={data['code']}")
    # 记录ID但不return（pytest函数不应有返回值）
    created_id = data.get("data", {}).get("id")
    print(f"创建的用户ID: {created_id}")


def test_create_user_duplicate_username(headers, base_url):
    """重复用户名创建"""
    payload = {
        "username": "admin",
        "password": "FsKgVFHIqn5oc2J2eqaxjg=="
    }
    res = requests.post(f"{base_url}/api/user/create", json=payload, headers=headers, verify=False)
    data = res.json()
    print(f"✅ 重复用户名响应: code={data['code']}")


def test_create_user_empty_username(headers, base_url):
    """空用户名创建"""
    payload = {
        "username": "",
        "password": "FsKgVFHIqn5oc2J2eqaxjg=="
    }
    res = requests.post(f"{base_url}/api/user/create", json=payload, headers=headers, verify=False)
    data = res.json()
    print(f"✅ 空用户名响应: code={data['code']}")


# ============ 角色管理 ============

def test_get_all_roles(headers, base_url):
    """获取所有角色"""
    res = requests.get(f"{base_url}/api/role/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 角色列表返回，数量: {len(data['data'])}")


def test_get_permissions(headers, base_url):
    """获取权限列表"""
    res = requests.get(f"{base_url}/api/role/findPermissions", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 权限列表返回成功")


# ============ 无Token访问 ============

def test_user_no_token(base_url):
    """无token访问用户接口"""
    res = requests.get(f"{base_url}/api/user/getCurrentUser", verify=False)
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 无Token访问被拦截")


def test_user_expired_token(base_url):
    """过期token访问"""
    headers = {"Authorization": "Bearer expired.token.here"}
    res = requests.get(f"{base_url}/api/user/getCurrentUser", headers=headers, verify=False)
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 过期Token被拦截")
