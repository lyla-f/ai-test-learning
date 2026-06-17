# test_17_term_extra.py - 术语管理剩余接口测试
import requests
import warnings
import time
warnings.filterwarnings("ignore")


# ================================================================
# 术语管理 term 剩余接口
# ================================================================

def test_term_create(headers, base_url):
    """创建术语"""
    payload = {
        "name": f"测试术语{int(time.time())}",
        "tw_name": "測試術語",
        "en_name": "Test Term",
        "sort": "1",
        "status": 1,
        "remark": "自动化测试创建"
    }
    res = requests.post(f"{base_url}/api/term/create", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 创建术语接口可达: {res.json()['code']}")


def test_term_update(headers, base_url):
    """更新术语"""
    payload = {"id": "non_exist_id", "name": "更新术语", "status": 1}
    res = requests.put(f"{base_url}/api/term/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新术语接口可达: {res.json()['code']}")


def test_term_delete(headers, base_url):
    """删除术语"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(f"{base_url}/api/term/delete", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 删除术语接口可达: {res.json()['code']}")


def test_term_find_atlas(headers, base_url):
    """获取术语图册"""
    res = requests.get(
        f"{base_url}/api/term/findAtlas",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 获取术语图册接口可达: {res.json()['code']}")


def test_term_find_by_id_parent(headers, base_url):
    """根据ID查询父级"""
    res = requests.get(
        f"{base_url}/api/term/findByIdParent",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 查询父级接口可达: {res.json()['code']}")


def test_term_find_children(headers, base_url):
    """根据ID获取所有子节点"""
    res = requests.get(
        f"{base_url}/api/term/findChildren",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 查询子节点接口可达: {res.json()['code']}")


def test_term_update_sort(headers, base_url):
    """更新术语排序"""
    payload = {
        "row1": {"id": "id1", "sort": "1"},
        "row2": {"id": "id2", "sort": "2"}
    }
    res = requests.post(f"{base_url}/api/term/updateSort", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新术语排序接口可达: {res.json()['code']}")


def test_term_save_atlas(headers, base_url):
    """保存术语图册"""
    payload = {"id": "non_exist_id", "atlas": []}
    res = requests.post(f"{base_url}/api/term/saveAtlas", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 保存术语图册接口可达: {res.json()['code']}")


def test_term_no_token(base_url):
    """无Token访问术语接口"""
    res = requests.get(f"{base_url}/api/term/findAll", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")
