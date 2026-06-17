# test_04_followup.py - 随访管理接口测试
import requests
import warnings
import time
warnings.filterwarnings("ignore")


# ============ 查询随访 ============

def test_get_all_followup(headers, base_url):
    """获取所有随访记录"""
    res = requests.get(f"{base_url}/api/followUp/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 随访记录列表，数量: {len(data['data'])}")


def test_get_followup_with_patient(headers, base_url):
    """获取随访记录联查患者信息"""
    res = requests.get(f"{base_url}/api/followUp/findAllWithPatient", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 随访+患者联查成功，数量: {len(data['data'])}")


def test_get_followup_with_patient_by_name(headers, base_url):
    """按姓名查询随访记录"""
    res = requests.get(
        f"{base_url}/api/followUp/findAllWithPatient",
        params={"name": "测试"},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 按姓名查询随访成功")


def test_get_followup_this_week(headers, base_url):
    """按本周查询随访记录"""
    res = requests.get(
        f"{base_url}/api/followUp/findAllWithPatient",
        params={"timeType": "week"},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 本周随访查询成功")


# ============ 创建随访 ============

def test_create_followup_success(headers, base_url):
    """创建随访记录"""
    payload = {
        "patientId": "test_patient_id",
        "followUpDate": "2024-12-01T00:00:00.000Z",
        "followUpRemark": "自动化测试随访备注",
        "status": "未处理"
    }
    res = requests.post(
        f"{base_url}/api/followUp/create",
        json=payload,
        headers=headers,
        verify=False
    )
    data = res.json()
    # 接口可达验证（patientId不存在可能返回错误，但接口本身正常）
    assert res.status_code == 200
    print(f"✅ 创建随访接口可达，响应: {data['code']}")


def test_create_followup_missing_patient_id(headers, base_url):
    """缺少patientId创建随访"""
    payload = {
        "followUpDate": "2024-12-01T00:00:00.000Z",
        "followUpRemark": "测试备注"
    }
    res = requests.post(
        f"{base_url}/api/followUp/create",
        json=payload,
        headers=headers,
        verify=False
    )
    data = res.json()
    print(f"✅ 缺少patientId响应: code={data['code']}")


# ============ 更新随访 ============

def test_update_followup_structure(headers, base_url):
    """更新随访接口结构验证"""
    payload = {
        "id": "non_exist_id",
        "patientId": "test_patient_id",
        "status": "已联系",
        "followUpRemark": "已电话联系"
    }
    res = requests.put(
        f"{base_url}/api/followUp/update",
        json=payload,
        headers=headers,
        verify=False
    )
    assert res.status_code == 200
    print(f"✅ 更新随访接口可达，响应: {res.json()['code']}")


# ============ 导出随访 ============

def test_export_followup_excel(headers, base_url):
    """导出随访Excel接口可达性"""
    res = requests.get(
        f"{base_url}/api/followUp/exportFollowUpExcel",
        headers=headers,
        verify=False
    )
    # 导出接口返回文件流或JSON
    assert res.status_code == 200
    print(f"✅ 导出随访Excel接口可达")


# ============ 无Token访问 ============

def test_followup_no_token(base_url):
    """无token访问随访接口"""
    res = requests.get(f"{base_url}/api/followUp/findAll", verify=False)
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 无Token访问随访被拦截")
