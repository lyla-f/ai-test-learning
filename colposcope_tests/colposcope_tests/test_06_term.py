# test_06_term.py - 术语管理接口测试
import requests
import warnings
warnings.filterwarnings("ignore")


# ============ 查询术语 ============

def test_get_all_terms(headers, base_url):
    """获取所有术语"""
    res = requests.get(f"{base_url}/api/term/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 术语列表返回，数量: {len(data['data'])}")


def test_get_term_tree(headers, base_url):
    """获取树形术语"""
    res = requests.get(f"{base_url}/api/term/findTree", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 树形术语返回成功")


def test_get_parent_terms(headers, base_url):
    """获取父节点术语"""
    res = requests.get(f"{base_url}/api/term/findParent", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 父节点术语返回成功")


def test_get_cytology_terms(headers, base_url):
    """查询细胞学术语"""
    res = requests.get(f"{base_url}/api/term/findCyto", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 细胞学术语返回成功")


def test_get_hpv_terms(headers, base_url):
    """查询HPV术语"""
    res = requests.get(f"{base_url}/api/term/findHpv", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ HPV术语返回成功")


def test_get_medical_history(headers, base_url):
    """获取病史/指征数据"""
    res = requests.get(f"{base_url}/api/term/getMedicalHistory", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 病史/指征数据返回成功")


def test_get_past_pathology_terms(headers, base_url):
    """查询既往病理术语-子宫颈"""
    res = requests.get(
        f"{base_url}/api/term/findPastPathology",
        params={"type": "cervix"},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 既往病理术语(子宫颈)返回成功")


def test_get_past_pathology_terms_vulva(headers, base_url):
    """查询既往病理术语-外阴"""
    res = requests.get(
        f"{base_url}/api/term/findPastPathology",
        params={"type": "vulva"},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 既往病理术语(外阴)返回成功")


def test_get_term_by_name(headers, base_url):
    """按名称查询术语"""
    res = requests.get(
        f"{base_url}/api/term/findByName",
        params={"name": "正常"},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 按名称查询术语成功")


def test_get_term_page(headers, base_url):
    """分页查询术语"""
    res = requests.get(
        f"{base_url}/api/term/findPage",
        params={"page": 1, "size": 10},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 分页术语返回成功")


# ============ 字典数据 ============

def test_get_dict_data_by_type(headers, base_url):
    """按类型获取字典数据"""
    res = requests.get(
        f"{base_url}/api/dictData/findDictDataByDictType",
        params={"dictType": "patient_source"},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 字典数据返回成功")


# ============ 无Token访问 ============

def test_term_no_token(base_url):
    """无token访问术语接口"""
    res = requests.get(f"{base_url}/api/term/findAll", verify=False)
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 无Token访问被拦截")
