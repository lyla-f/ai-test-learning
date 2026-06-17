# test_09_backup_restore.py - 备份恢复接口测试
import requests
import warnings
warnings.filterwarnings("ignore")


# ================================================================
# 备份管理 backup (4个接口)
# ================================================================

def test_backup_list(headers, base_url):
    """获取备份列表"""
    res = requests.get(f"{base_url}/api/backup/list", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 备份列表，数量: {len(data['data'])}")


def test_backup_create(headers, base_url):
    """创建全量备份（仅管理员）"""
    res = requests.post(f"{base_url}/api/backup/create", json={}, headers=headers, verify=False)
    data = res.json()
    assert res.status_code == 200
    print(f"✅ 创建备份响应: code={data['code']}, msg={data['msg']}")


def test_backup_download_invalid_id(headers, base_url):
    """下载备份文件（无效ID）"""
    res = requests.get(
        f"{base_url}/api/backup/download/non_exist_id",
        headers=headers, verify=False
    )
    assert res.status_code == 200 or res.status_code == 404
    print(f"✅ 下载备份接口可达，状态码: {res.status_code}")


def test_backup_delete_invalid_id(headers, base_url):
    """删除备份（无效ID）"""
    res = requests.delete(
        f"{base_url}/api/backup/non_exist_id",
        headers=headers, verify=False
    )
    assert res.status_code == 200 or res.status_code == 404
    print(f"✅ 删除备份接口可达，响应: {res.status_code}")


def test_backup_no_token(base_url):
    """无Token访问备份接口"""
    res = requests.get(f"{base_url}/api/backup/list", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")


# ================================================================
# 恢复管理 restore (4个接口)
# ================================================================

def test_restore_history(headers, base_url):
    """获取恢复历史记录"""
    res = requests.get(f"{base_url}/api/restore/history", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 恢复历史记录返回成功")


def test_restore_preview(headers, base_url):
    """预览恢复内容"""
    res = requests.post(f"{base_url}/api/restore/preview", json={}, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 预览恢复接口可达: {res.json()['code']}")


def test_restore_upload(headers, base_url):
    """上传备份文件接口可达（不实际上传）"""
    res = requests.post(f"{base_url}/api/restore/upload", headers=headers, verify=False)
    assert res.status_code == 200 or res.status_code == 400
    print(f"✅ 上传备份接口可达，状态码: {res.status_code}")


def test_restore_execute(headers, base_url):
    """执行恢复接口可达（仅管理员）"""
    res = requests.post(f"{base_url}/api/restore/execute", json={}, headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 执行恢复接口可达: {res.json()['code']}")


def test_restore_no_token(base_url):
    """无Token访问恢复接口"""
    res = requests.get(f"{base_url}/api/restore/history", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")
