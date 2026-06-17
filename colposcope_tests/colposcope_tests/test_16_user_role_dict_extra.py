# test_16_user_role_dict_extra.py - 用户/角色/字典剩余接口测试
import requests
import warnings
import time
warnings.filterwarnings("ignore")


# ================================================================
# 用户管理剩余接口
# ================================================================

def test_user_update(headers, base_url):
    """更新用户信息"""
    payload = {"id": "non_exist_id", "autograph": "测试更新"}
    res = requests.put(f"{base_url}/api/user/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新用户接口可达: {res.json()['code']}")


def test_user_reset_password(headers, base_url):
    """重置密码接口可达"""
    payload = {
        "id": "non_exist_id",
        "oldPassword": "FsKgVFHIqn5oc2J2eqaxjg==",
        "newPassword": "FsKgVFHIqn5oc2J2eqaxjg=="
    }
    res = requests.put(f"{base_url}/api/user/resetPassword", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 重置密码接口可达: {res.json()['code']}")


def test_user_delete(headers, base_url):
    """删除用户接口可达"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(f"{base_url}/api/user/delete", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 删除用户接口可达: {res.json()['code']}")


def test_user_find_by_id(headers, base_url):
    """查询单个用户"""
    res = requests.get(
        f"{base_url}/api/user/findById",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按ID查询用户接口可达: {res.json()['code']}")


# ================================================================
# 角色管理剩余接口
# ================================================================

def test_role_create(headers, base_url):
    """创建角色"""
    payload = {"name": f"测试角色{int(time.time())}", "description": "自动化测试角色", "status": 1}
    res = requests.post(f"{base_url}/api/role/create", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 创建角色接口可达: {res.json()['code']}")


def test_role_find_by_id(headers, base_url):
    """获取单个角色"""
    res = requests.get(
        f"{base_url}/api/role/findById",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按ID查询角色接口可达: {res.json()['code']}")


def test_role_find_page(headers, base_url):
    """分页获取角色"""
    res = requests.get(
        f"{base_url}/api/role/findPage",
        params={"page": 1, "size": 10},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 分页角色列表接口可达: {res.json()['code']}")


def test_role_update(headers, base_url):
    """更新角色"""
    payload = {"id": "non_exist_id", "description": "更新测试角色"}
    res = requests.put(f"{base_url}/api/role/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新角色接口可达: {res.json()['code']}")


def test_role_delete(headers, base_url):
    """删除角色"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(f"{base_url}/api/role/delete", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 删除角色接口可达: {res.json()['code']}")


# ================================================================
# 字典类型 dictType (5个接口)
# ================================================================

def test_dict_type_find_all(headers, base_url):
    """获取所有字典类型"""
    res = requests.get(f"{base_url}/api/dictType/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 字典类型列表，数量: {len(data['data'])}")


def test_dict_type_find_by_id(headers, base_url):
    """获取单个字典类型"""
    res = requests.get(
        f"{base_url}/api/dictType/findById",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按ID查询字典类型接口可达: {res.json()['code']}")


def test_dict_type_create(headers, base_url):
    """创建字典类型"""
    payload = {"dictType": f"test_type_{int(time.time())}", "name": "测试类型", "status": 1}
    res = requests.post(f"{base_url}/api/dictType/createDictType", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 创建字典类型接口可达: {res.json()['code']}")


def test_dict_type_update(headers, base_url):
    """更新字典类型"""
    payload = {"id": "non_exist_id", "name": "更新类型"}
    res = requests.put(f"{base_url}/api/dictType/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新字典类型接口可达: {res.json()['code']}")


def test_dict_type_delete(headers, base_url):
    """删除字典类型"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(f"{base_url}/api/dictType/delete", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 删除字典类型接口可达: {res.json()['code']}")


# ================================================================
# 字典数据 dictData 剩余接口
# ================================================================

def test_dict_data_find_all(headers, base_url):
    """获取所有字典数据"""
    res = requests.get(f"{base_url}/api/dictData/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 字典数据列表，数量: {len(data['data'])}")


def test_dict_data_find_by_id(headers, base_url):
    """获取单个字典数据"""
    res = requests.get(
        f"{base_url}/api/dictData/findById",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按ID查询字典数据接口可达: {res.json()['code']}")


def test_dict_data_find_by_types(headers, base_url):
    """根据dictTypes查询dictData"""
    res = requests.get(
        f"{base_url}/api/dictData/findDictDataByDictTypes",
        params={"dictType": "patient_source"},
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 按类型列表查询字典数据成功")


def test_dict_data_create(headers, base_url):
    """创建字典数据"""
    payload = {
        "sort": 1,
        "dictType": "test_type",
        "label": "测试标签",
        "value": "test_value",
        "status": 1
    }
    res = requests.post(
        f"{base_url}/api/dictData/createDictData",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 创建字典数据接口可达: {res.json()['code']}")


def test_dict_data_update(headers, base_url):
    """更新字典数据"""
    payload = {"id": "non_exist_id", "label": "更新标签"}
    res = requests.put(f"{base_url}/api/dictData/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新字典数据接口可达: {res.json()['code']}")


def test_dict_data_delete(headers, base_url):
    """删除字典数据"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(f"{base_url}/api/dictData/delete", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 删除字典数据接口可达: {res.json()['code']}")


def test_dict_no_token(base_url):
    """无Token访问字典接口（需认证的接口）"""
    res = requests.get(f"{base_url}/api/dictData/findAll", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")
