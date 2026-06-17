# test_15_report_extra.py - 报告管理剩余接口测试
import requests
import warnings
warnings.filterwarnings("ignore")


# ================================================================
# 报告模板 report 剩余接口
# ================================================================

def test_report_create(headers, base_url):
    """创建报告模板"""
    payload = {
        "title": "测试报告模板",
        "caseType": "colposcopy",
        "layoutConfig": {},
        "content": {},
        "infoSelect": {},
        "printConfig": {}
    }
    res = requests.post(f"{base_url}/api/report/create", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 创建报告模板接口可达: {res.json()['code']}")


def test_report_update(headers, base_url):
    """更新报告模板"""
    payload = {"id": "non_exist_id", "title": "更新报告模板"}
    res = requests.put(f"{base_url}/api/report/update", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 更新报告模板接口可达: {res.json()['code']}")


def test_report_delete(headers, base_url):
    """删除报告模板"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(f"{base_url}/api/report/delete", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 删除报告模板接口可达: {res.json()['code']}")


# ================================================================
# 报告修订版本 report-revision 剩余接口
# ================================================================

def test_report_revision_create(headers, base_url):
    """创建修订版本"""
    payload = {
        "reportId": "non_exist_report_id",
        "patientId": "non_exist_patient_id",
        "description": "测试修订版本",
        "layoutConfig": {},
        "content": {},
        "infoSelect": {},
        "printConfig": {},
        "isCurrent": True
    }
    res = requests.post(
        f"{base_url}/api/report-revision/create",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 创建修订版本接口可达: {res.json()['code']}")


def test_report_revision_find_by_id(headers, base_url):
    """根据ID获取修订版本"""
    res = requests.get(
        f"{base_url}/api/report-revision/findById",
        params={"id": "non_exist_id", "patientId": "non_exist_patient_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按ID查询修订版本接口可达: {res.json()['code']}")


def test_report_revision_update(headers, base_url):
    """更新修订版本内容"""
    payload = {
        "id": "non_exist_id",
        "patientId": "non_exist_patient_id",
        "isCurrent": True
    }
    res = requests.put(
        f"{base_url}/api/report-revision/update",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 更新修订版本接口可达: {res.json()['code']}")


def test_report_revision_set_current(headers, base_url):
    """设置当前修订版本"""
    payload = {"id": "non_exist_id", "patientId": "non_exist_patient_id"}
    res = requests.put(
        f"{base_url}/api/report-revision/set-current",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 设置当前修订版本接口可达: {res.json()['code']}")


def test_report_revision_create_with_images(headers, base_url):
    """创建修订版本并批量创建图像记录"""
    payload = {
        "reportId": "non_exist_report_id",
        "patientId": "non_exist_patient_id",
        "isCurrent": True,
        "images": []
    }
    res = requests.post(
        f"{base_url}/api/report-revision/createWithImages",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 创建修订版本含图像接口可达: {res.json()['code']}")


def test_report_revision_update_with_images(headers, base_url):
    """更新修订版本并更新图像记录"""
    payload = {
        "id": "non_exist_id",
        "patientId": "non_exist_patient_id",
        "images": []
    }
    res = requests.put(
        f"{base_url}/api/report-revision/updateWithImages",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 更新修订版本含图像接口可达: {res.json()['code']}")


# ================================================================
# 报告图片 report-revision-image 剩余接口
# ================================================================

def test_report_image_create(headers, base_url):
    """创建图片记录"""
    payload = {
        "reportRevisionId": "non_exist_revision_id",
        "originalImagePath": "/test/path/image.jpg",
        "drawingObjectsJson": {}
    }
    res = requests.post(
        f"{base_url}/api/report-revision-image/create",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 创建图片记录接口可达: {res.json()['code']}")


def test_report_image_create_batch(headers, base_url):
    """批量创建图片记录"""
    payload = [{
        "reportRevisionId": "non_exist_revision_id",
        "originalImagePath": "/test/path/image.jpg",
        "drawingObjectsJson": {}
    }]
    res = requests.post(
        f"{base_url}/api/report-revision-image/createBatch",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 批量创建图片记录接口可达: {res.json()['code']}")


def test_report_image_find_by_id(headers, base_url):
    """根据ID查询图片记录"""
    res = requests.get(
        f"{base_url}/api/report-revision-image/findById",
        params={"id": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按ID查询图片记录接口可达: {res.json()['code']}")


def test_report_image_update(headers, base_url):
    """更新图片记录"""
    payload = {"id": "non_exist_id", "sort": "1"}
    res = requests.put(
        f"{base_url}/api/report-revision-image/update",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 更新图片记录接口可达: {res.json()['code']}")


def test_report_image_delete(headers, base_url):
    """删除图片记录"""
    payload = {"id": "non_exist_id"}
    res = requests.delete(
        f"{base_url}/api/report-revision-image/delete",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 删除图片记录接口可达: {res.json()['code']}")


def test_report_image_delete_by_revision(headers, base_url):
    """删除指定修订版本所有图片"""
    res = requests.delete(
        f"{base_url}/api/report-revision-image/deleteByReportRevisionId",
        params={"reportRevisionId": "non_exist_id"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按修订版本删除图片接口可达: {res.json()['code']}")


def test_report_no_token(base_url):
    """无Token访问报告接口"""
    res = requests.get(f"{base_url}/api/report/findAll", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")
