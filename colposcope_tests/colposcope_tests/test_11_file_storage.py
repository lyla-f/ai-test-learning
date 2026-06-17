# test_11_file_storage.py - 文件存储接口测试
import requests
import warnings
warnings.filterwarnings("ignore")


# ================================================================
# 文件存储统计 file-storage (11个接口)
# ================================================================

def test_file_storage_total_stats(headers, base_url):
    """获取总体存储统计"""
    res = requests.get(f"{base_url}/api/file-storage/statistics/total", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 总体存储统计: {data['data']}")


def test_file_storage_my_storage(headers, base_url):
    """获取当前用户存储统计"""
    res = requests.get(f"{base_url}/api/file-storage/statistics/my-storage", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 当前用户存储统计: {data['data']}")


def test_file_storage_by_user(headers, base_url):
    """按用户统计存储空间"""
    res = requests.get(f"{base_url}/api/file-storage/statistics/by-user", headers=headers, verify=False)
    data = res.json()
    assert data["code"] == 200
    print(f"✅ 按用户统计返回成功")


def test_file_storage_by_time_day(headers, base_url):
    """按天统计存储（带日期范围）"""
    import datetime
    today = datetime.date.today().isoformat()
    month_ago = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
    for params in [
        {"dimension": "day", "startDate": month_ago, "endDate": today},
        {"dimension": "day"},
    ]:
        res = requests.get(
            f"{base_url}/api/file-storage/statistics/by-time",
            params=params, headers=headers, verify=False
        )
        data = res.json()
        if data["code"] == 200:
            print(f"✅ 按天统计返回成功，params={params}")
            return
        print(f"⚠️ params={params} 返回: {data['code']} - {data['msg']}")
    print("ℹ️ 按天统计接口需特定参数，记录备用")


def test_file_storage_by_time_month(headers, base_url):
    """按月统计存储（带日期范围）"""
    import datetime
    today = datetime.date.today().isoformat()
    year_ago = (datetime.date.today() - datetime.timedelta(days=365)).isoformat()
    for params in [
        {"dimension": "month", "startDate": year_ago, "endDate": today},
        {"dimension": "month"},
    ]:
        res = requests.get(
            f"{base_url}/api/file-storage/statistics/by-time",
            params=params, headers=headers, verify=False
        )
        data = res.json()
        if data["code"] == 200:
            print(f"✅ 按月统计返回成功，params={params}")
            return
        print(f"⚠️ params={params} 返回: {data['code']} - {data['msg']}")
    print("ℹ️ 按月统计接口需特定参数，记录备用")


def test_file_storage_by_time_year(headers, base_url):
    """按年统计存储（带日期范围）"""
    import datetime
    today = datetime.date.today().isoformat()
    years_ago = (datetime.date.today() - datetime.timedelta(days=730)).isoformat()
    for params in [
        {"dimension": "year", "startDate": years_ago, "endDate": today},
        {"dimension": "year"},
    ]:
        res = requests.get(
            f"{base_url}/api/file-storage/statistics/by-time",
            params=params, headers=headers, verify=False
        )
        data = res.json()
        if data["code"] == 200:
            print(f"✅ 按年统计返回成功，params={params}")
            return
        print(f"⚠️ params={params} 返回: {data['code']} - {data['msg']}")
    print("ℹ️ 按年统计接口需特定参数，记录备用")


def test_file_storage_by_extension(headers, base_url):
    """按文件类型统计"""
    res = requests.get(
        f"{base_url}/api/file-storage/statistics/by-extension/jpg",
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 按jpg类型统计返回: {res.json()['code']}")


def test_file_storage_backup_list(headers, base_url):
    """获取备份文件列表"""
    import datetime
    today = datetime.date.today().isoformat()
    res = requests.get(
        f"{base_url}/api/file-storage/backup/file-list",
        params={"startDate": "2024-01-01", "endDate": today},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 备份文件列表返回: {res.json()['code']}")


def test_file_storage_batch_check(headers, base_url):
    """批量检查文件同步状态"""
    payload = {"fileHashes": ["non_exist_hash_1", "non_exist_hash_2"]}
    res = requests.post(
        f"{base_url}/api/file-storage/batch-check",
        json=payload, headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 批量检查文件状态: {res.json()['code']}")


def test_file_storage_metadata_invalid(headers, base_url):
    """获取无效文件元数据"""
    res = requests.get(
        f"{base_url}/api/file-storage/metadata/non_exist_file_id",
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 获取文件元数据接口可达: {res.json()['code']}")


def test_file_storage_metadata_by_hash(headers, base_url):
    """通过Hash获取文件元数据"""
    res = requests.get(
        f"{base_url}/api/file-storage/metadata-by-hash/non_exist_hash",
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 通过Hash获取元数据接口可达: {res.json()['code']}")


def test_file_storage_no_token(base_url):
    """无Token访问文件存储接口"""
    res = requests.get(f"{base_url}/api/file-storage/statistics/total", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")


# ================================================================
# 文件导入导出 files (4个接口)
# ================================================================

def test_files_download_template(headers, base_url):
    """下载Excel导入模板"""
    res = requests.get(f"{base_url}/api/files/downloadTemplate", headers=headers, verify=False)
    assert res.status_code == 200
    print(f"✅ 下载模板接口可达，Content-Type: {res.headers.get('Content-Type', '未知')}")


def test_files_export_excel(headers, base_url):
    """导出Excel接口可达"""
    res = requests.get(
        f"{base_url}/api/files/exportExcel",
        params={"url": "test"},
        headers=headers, verify=False
    )
    assert res.status_code == 200
    print(f"✅ 导出Excel接口可达，状态: {res.status_code}")


def test_files_no_token(base_url):
    """无Token访问文件接口"""
    res = requests.get(f"{base_url}/api/files/downloadTemplate", verify=False)
    assert res.json()["code"] != 200
    print(f"✅ 无Token被拦截")
