# test_10_certificate_sys.py - 证书管理 + 系统维护接口测试
import requests
import warnings
warnings.filterwarnings("ignore")


# ================================================================
# 证书管理 certificate (5个接口)
# ================================================================

def test_certificate_ca(base_url):
    """获取CA证书（白名单接口，无需Token）"""
    res = requests.get(f"{base_url}/api/certificate/ca", verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ CA证书获取成功")


def test_certificate_request(base_url):
    """申请证书（白名单接口）"""
    payload = {"deviceId": "test_device", "deviceName": "测试设备"}
    res = requests.post(f"{base_url}/api/certificate/request", json=payload, verify=False)
    assert res.status_code == 200
    print(f"✅ 申请证书接口可达: {res.json()['code']}")


def test_certificate_approve(headers, base_url):
    """审批证书"""
    payload = {"certificateId": "non_exist_id", "approved": True}
    res = requests.post(f"{base_url}/api/certificate/approve", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 审批证书接口可达: {res.json()['code']}")


def test_certificate_renew(headers, base_url):
    """续期证书"""
    payload = {"certificateId": "non_exist_id"}
    res = requests.post(f"{base_url}/api/certificate/renew", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 续期证书接口可达: {res.json()['code']}")


def test_certificate_revoke(headers, base_url):
    """吊销证书"""
    payload = {"certificateId": "non_exist_id", "reason": "测试吊销"}
    res = requests.post(f"{base_url}/api/certificate/revoke", json=payload, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 吊销证书接口可达: {res.json()['code']}")


# ================================================================
# 系统维护 sys (2个接口)
# ================================================================

def test_sys_check_maintain_password(headers, base_url):
    """验证维护密码"""
    payload = {"password": "wrong_maintain_password"}
    res = requests.post(
        f"{base_url}/api/sys/checkMaintainPassword",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 验证维护密码接口可达: {res.json()['code']}")


def test_sys_set_maintain_password(headers, base_url):
    """设置维护密码接口可达"""
    payload = {"password": "test_maintain_pwd"}
    res = requests.post(
        f"{base_url}/api/sys/setMaintainPassword",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 设置维护密码接口可达: {res.json()['code']}")


def test_sys_no_token(base_url):
    """无Token访问系统维护接口"""
    payload = {"password": "test"}
    res = requests.post(f"{base_url}/api/sys/checkMaintainPassword", json=payload, verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")


# ================================================================
# 根路径 root (1个接口)
# ================================================================

def test_root_health(base_url):
    """首页健康检查"""
    res = requests.get(f"{base_url}/", verify=False)
    assert res.status_code == 200
    print(f"✅ 首页接口可达")
