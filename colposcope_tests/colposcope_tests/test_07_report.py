# test_07_report.py - 报告管理接口测试
import requests
import warnings
warnings.filterwarnings("ignore")


# ============ 查询报告 ============

def test_get_all_reports(headers, base_url):
    """获取所有报告模板"""
    res = requests.get(f"{base_url}/api/report/findAll", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 报告模板列表，数量: {len(data['data'])}")


def test_get_report_by_invalid_id(headers, base_url):
    """用不存在ID查询报告"""
    res = requests.get(
        f"{base_url}/api/report/findById",
        params={"id": "non_exist_id"},
        headers=headers,
        verify=False
    )
    data = res.json()
    print(f"✅ 不存在ID查询响应: code={data['code']}")


# ============ 报告修订版本 ============

def test_get_report_revision_list(headers, base_url):
    """获取报告修订版本列表"""
    res = requests.get(
        f"{base_url}/api/report-revision/list",
        params={"reportId": "test_report_id", "patientId": "test_patient_id"},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert res.status_code == 200
    print(f"✅ 报告修订版本接口可达，响应: {data['code']}")


def test_get_current_revision(headers, base_url):
    """获取当前修订版本"""
    res = requests.get(
        f"{base_url}/api/report-revision/current",
        params={"reportId": "test_report_id", "patientId": "test_patient_id"},
        headers=headers,
        verify=False
    )
    data = res.json()
    assert res.status_code == 200
    print(f"✅ 当前修订版本接口可达，响应: {data['code']}")


# ============ 文件下载 ============

def test_download_excel_template(headers, base_url):
    """下载Excel导入模板"""
    res = requests.get(
        f"{base_url}/api/files/downloadTemplate",
        headers=headers,
        verify=False
    )
    assert res.status_code == 200
    print(f"✅ 下载Excel模板接口可达，内容类型: {res.headers.get('Content-Type', '未知')}")


# ============ 系统健康检查 ============

def test_health_check(base_url):
    """系统健康检查（白名单接口，无需token）"""
    res = requests.get(f"{base_url}/api/mdns/health", verify=False)
    data = res.json()
    assert data["code"] == 200
    assert data["data"]["status"] == "healthy"
    print(f"✅ 系统健康，类型: {data['data'].get('nodeType', '未知')}")


def test_system_identity(base_url):
    """获取系统标识（白名单接口）"""
    res = requests.get(f"{base_url}/api/mdns/identity", verify=False)
    data = res.json()
    assert data["code"] == 200
    assert "appId" in data["data"]
    print(f"✅ 系统标识: {data['data']['appId']} v{data['data'].get('version', '未知')}")


# ============ 报告图片 ============

def test_report_revision_image_count(headers, base_url):
    """统计报告图片数量接口"""
    res = requests.get(
        f"{base_url}/api/report-revision-image/countByReportRevisionId",
        params={"reportRevisionId": "test_id"},
        headers=headers,
        verify=False
    )
    assert res.status_code == 200
    print(f"✅ 统计图片数量接口可达，响应: {res.json()['code']}")


def test_get_images_by_revision(headers, base_url):
    """按修订版本ID查询图片"""
    res = requests.get(
        f"{base_url}/api/report-revision-image/findByReportRevisionId",
        params={"reportRevisionId": "test_id"},
        headers=headers,
        verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按修订版本查询图片接口可达，响应: {res.json()['code']}")


# ============ 无Token访问 ============

def test_report_no_token(base_url):
    """无token访问报告接口"""
    res = requests.get(f"{base_url}/api/report/findAll", verify=False)
    data = res.json()
    assert data["code"] != 200
    print(f"✅ 无Token访问报告被拦截")
