# test_14_patient_extra.py - 病人管理剩余接口 + 医师申请接口测试
import requests
import warnings
import time
warnings.filterwarnings("ignore")


# ================================================================
# 病人管理剩余接口
# ================================================================

def test_patient_find_by_id(headers, base_url):
    """获取患者详细信息包含病例"""
    res = requests.get(
        f"{base_url}/api/patient/findById",
        params={"id": "non_exist_patient_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按ID查询患者接口可达: {res.json()['code']}")


def test_patient_get_with_revision(headers, base_url):
    """查询单个病人信息联查修订版本"""
    res = requests.get(
        f"{base_url}/api/patient/getPatientWithRevision",
        params={"patientId": "non_exist_patient_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 查询患者含修订接口可达: {res.json()['code']}")


def test_patient_start_inspection(headers, base_url):
    """开始检查现有患者接口可达"""
    payload = {"patientId": "non_exist_patient_id"}
    res = requests.post(
        f"{base_url}/api/patient/startInspection",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 开始检查接口可达: {res.json()['code']}")


def test_patient_update(headers, base_url):
    """更新患者和病例信息"""
    payload = {"id": "non_exist_id", "name": "更新测试"}
    res = requests.post(
        f"{base_url}/api/patient/update",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 更新患者接口可达: {res.json()['code']}")


# ================================================================
# 公共接口剩余
# ================================================================

def test_common_confirm_patient_id(headers, base_url):
    """确认病人ID"""
    payload = {"patientId": "TEST_CONFIRM_001"}
    res = requests.post(
        f"{base_url}/api/common/confirmPatientid",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 确认病人ID接口可达: {res.json()['code']}")


def test_common_release_patient_id(headers, base_url):
    """释放病人ID"""
    payload = {"patientId": "TEST_RELEASE_001"}
    res = requests.post(
        f"{base_url}/api/common/releasePatientid",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 释放病人ID接口可达: {res.json()['code']}")


# ================================================================
# 医师申请 physicianApplication (3个接口)
# ================================================================

def test_physician_find_by_current_user(headers, base_url):
    """获取当前用户的医师申请列表"""
    res = requests.get(
        f"{base_url}/api/physicianApplication/findByCurrentUser",
        headers=headers, verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 当前用户医师申请列表: {data['data']}")


def test_physician_create(headers, base_url):
    """创建医师申请"""
    payload = {
        "name": f"测试申请{int(time.time())}",
        "type": "license",
        "description": "自动化测试申请",
        "userId": "test_user_id"
    }
    res = requests.post(
        f"{base_url}/api/physicianApplication/create",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 创建医师申请接口可达: {res.json()['code']}")


def test_physician_delete(headers, base_url):
    """删除医师申请"""
    res = requests.delete(
        f"{base_url}/api/physicianApplication/delete",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 删除医师申请接口可达: {res.json()['code']}")


def test_physician_no_token(base_url):
    """无Token访问医师申请接口"""
    res = requests.get(
        f"{base_url}/api/physicianApplication/findByCurrentUser",
        verify=False
    )
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")
