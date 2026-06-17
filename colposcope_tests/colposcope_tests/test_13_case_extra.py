# test_13_case_extra.py - 病例管理剩余接口测试
import requests
import warnings
import time
warnings.filterwarnings("ignore")


# ================================================================
# 病例 CRUD 剩余接口
# ================================================================

def test_case_create(headers, base_url):
    """创建病例接口可达"""
    payload = {"patientId": "test_patient_id", "caseType": 1}
    res = requests.post(f"{base_url}/api/case/create", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 创建病例接口可达: {res.json()['code']}")


def test_case_find_by_id(headers, base_url):
    """根据ID获取病例"""
    res = requests.get(
        f"{base_url}/api/case/findById",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按ID查询病例接口可达: {res.json()['code']}")


def test_case_find_by_patient_id(headers, base_url):
    """根据患者ID获取病例列表"""
    res = requests.get(
        f"{base_url}/api/case/findByPatientId",
        params={"patientId": "non_exist_patient_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按患者ID查询病例: {res.json()['code']}")


def test_case_find_by_patient_id_with_revision(headers, base_url):
    """根据患者ID获取病例列表（包含修订版本）"""
    res = requests.get(
        f"{base_url}/api/case/findByPatientIdWithRevision",
        params={"patientId": "non_exist_patient_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按患者ID查询病例含修订: {res.json()['code']}")


def test_case_get_case_with_patient(headers, base_url):
    """获取病例详情包含患者信息"""
    res = requests.get(
        f"{base_url}/api/case/getCaseWithPatient",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 获取病例+患者接口可达: {res.json()['code']}")


def test_case_get_field_options(headers, base_url):
    """获取字段选项"""
    res = requests.get(
        f"{base_url}/api/case/getFieldOptions",
        params={"fieldName": "diagnosis"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 获取字段选项接口可达: {res.json()['code']}")


def test_case_update(headers, base_url):
    """更新病例接口可达"""
    payload = {"id": "non_exist_id", "remark": "测试更新"}
    res = requests.put(f"{base_url}/api/case/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新病例接口可达: {res.json()['code']}")


def test_case_update_pathology_info(headers, base_url):
    """更新病理信息"""
    payload = {"id": "non_exist_id", "pathologyInfo": "测试病理"}
    res = requests.post(
        f"{base_url}/api/case/updatePathologyInfo",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 更新病理信息接口可达: {res.json()['code']}")


def test_case_update_sort(headers, base_url):
    """更新排序"""
    payload = {
        "row1": {"id": "id1", "sort": "1"},
        "row2": {"id": "id2", "sort": "2"}
    }
    res = requests.post(
        f"{base_url}/api/case/updateSort",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 更新排序接口可达: {res.json()['code']}")


def test_case_restore_cases(headers, base_url):
    """恢复已删除病历"""
    payload = {"caseIds": ["non_exist_id"]}
    res = requests.post(
        f"{base_url}/api/case/restoreCases",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 恢复已删除病历接口可达: {res.json()['code']}")


# ================================================================
# 病例重点关注操作
# ================================================================

def test_case_get_key_focuses(headers, base_url):
    """获取病例重点关注"""
    res = requests.get(
        f"{base_url}/api/case/getCaseKeyFocuses",
        params={"caseId": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 获取病例重点关注接口可达: {res.json()['code']}")


def test_case_set_key_focus(headers, base_url):
    """设置病例重点关注"""
    payload = {"caseId": "non_exist_id", "keyFocusId": "non_exist_focus_id"}
    res = requests.post(
        f"{base_url}/api/case/setCaseKeyFocus",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 设置病例重点关注接口可达: {res.json()['code']}")


def test_case_toggle_key_focus(headers, base_url):
    """切换病例重点关注状态"""
    payload = {"caseId": "non_exist_id", "keyFocusId": "non_exist_focus_id"}
    res = requests.post(
        f"{base_url}/api/case/toggleCaseKeyFocus",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 切换病例重点关注接口可达: {res.json()['code']}")


def test_case_toggle_patient_key_focus(headers, base_url):
    """切换患者重点关注（兼容接口）"""
    payload = {"patientId": "non_exist_id", "keyFocusId": "non_exist_focus_id"}
    res = requests.post(
        f"{base_url}/api/case/togglePatientKeyFocus",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 切换患者重点关注接口可达: {res.json()['code']}")


def test_case_remove_key_focus(headers, base_url):
    """移除病例重点关注"""
    payload = {"caseId": "non_exist_id", "keyFocusId": "non_exist_focus_id"}
    res = requests.delete(
        f"{base_url}/api/case/removeCaseKeyFocus",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 移除病例重点关注接口可达: {res.json()['code']}")


def test_case_delete(headers, base_url):
    """删除病例接口可达"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(f"{base_url}/api/case/delete", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 删除病例接口可达: {res.json()['code']}")
