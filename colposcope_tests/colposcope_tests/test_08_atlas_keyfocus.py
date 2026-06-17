# test_08_atlas_keyfocus.py - 图册管理 + 重点关注接口测试
import requests
import warnings
import time
warnings.filterwarnings("ignore")


# ================================================================
# 图册管理 atlas (5个接口)
# ================================================================

def test_atlas_find_all(headers, base_url):
    """获取所有图册"""
    res = requests.get(f"{base_url}/api/atlas/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 图册列表，数量: {len(data['data'])}")


def test_atlas_create(headers, base_url):
    """创建图册"""
    payload = {"name": f"测试图册{int(time.time())}", "remark": "自动化测试"}
    res = requests.post(f"{base_url}/api/atlas/create", json=payload, headers=headers, verify=False)
    data = res.json()
    assert res.status_code == 200
    print(f"✅ 创建图册响应: code={data['code']}")


def test_atlas_find_by_id_invalid(headers, base_url):
    """用无效ID查询图册"""
    res = requests.get(
        f"{base_url}/api/atlas/findById",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 无效ID查询图册响应: {res.json()['code']}")


def test_atlas_update(headers, base_url):
    """更新图册接口可达"""
    payload = {"id": "non_exist_id", "name": "更新测试"}
    res = requests.put(f"{base_url}/api/atlas/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新图册接口可达: {res.json()['code']}")


def test_atlas_delete(headers, base_url):
    """删除图册接口可达"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(f"{base_url}/api/atlas/delete", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 删除图册接口可达: {res.json()['code']}")


def test_atlas_no_token(base_url):
    """无Token访问图册接口"""
    res = requests.get(f"{base_url}/api/atlas/findAll", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")


# ================================================================
# 重点关注 keyFocus (5个接口)
# ================================================================

def test_keyfocus_find_all(headers, base_url):
    """获取所有重点关注项"""
    res = requests.get(f"{base_url}/api/keyFocus/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 重点关注列表，数量: {len(data['data'])}")


def test_keyfocus_create(headers, base_url):
    """创建重点关注项"""
    payload = {"label": f"测试关注{int(time.time())}", "color": "#FF0000", "sort": 1, "status": 1}
    res = requests.post(f"{base_url}/api/keyFocus/create", json=payload, headers=headers, verify=False)
    data = res.json()
    assert res.status_code == 200
    print(f"✅ 创建重点关注响应: code={data['code']}")


def test_keyfocus_save_list(headers, base_url):
    """批量保存重点关注项"""
    payload = [{"label": f"批量关注{int(time.time())}", "color": "#00FF00", "sort": 2, "status": 1}]
    res = requests.post(f"{base_url}/api/keyFocus/saveList", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 批量保存重点关注响应: {res.json()['code']}")


def test_keyfocus_update(headers, base_url):
    """更新重点关注项"""
    payload = {"id": "non_exist_id", "label": "更新关注", "color": "#0000FF", "sort": 1, "status": 1}
    res = requests.put(f"{base_url}/api/keyFocus/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新重点关注响应: {res.json()['code']}")


def test_keyfocus_delete(headers, base_url):
    """删除重点关注项"""
    res = requests.delete(
        f"{base_url}/api/keyFocus/delete",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 删除重点关注响应: {res.json()['code']}")


def test_keyfocus_no_token(base_url):
    """无Token访问重点关注"""
    res = requests.get(f"{base_url}/api/keyFocus/findAll", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")
