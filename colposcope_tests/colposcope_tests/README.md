# 阴道镜系统 - 接口自动化测试（全量覆盖版）

## 覆盖情况

| 文件 | 模块 | 接口数 |
|------|------|--------|
| test_01_login.py | 登录 | 10个用例 |
| test_02_patient.py | 病人管理 | 10个用例 |
| test_03_case.py | 病例管理 | 10个用例 |
| test_04_followup.py | 随访管理 | 10个用例 |
| test_05_user.py | 用户管理 | 12个用例 |
| test_06_term.py | 术语管理 | 14个用例 |
| test_07_report.py | 报告+健康检查 | 12个用例 |
| test_08_atlas_keyfocus.py | 图册+重点关注 | 12个用例 |
| test_09_backup_restore.py | 备份+恢复 | 10个用例 |
| test_10_certificate_sys.py | 证书+系统维护 | 9个用例 |
| test_11_file_storage.py | 文件存储 | 15个用例 |
| test_12_sync.py | 数据同步 | 18个用例 |
| test_13_case_extra.py | 病例剩余接口 | 16个用例 |
| test_14_patient_extra.py | 病人剩余+医师申请 | 10个用例 |
| test_15_report_extra.py | 报告剩余接口 | 16个用例 |
| test_16_user_role_dict_extra.py | 用户/角色/字典剩余 | 18个用例 |
| test_17_term_extra.py | 术语剩余接口 | 9个用例 |
| **合计** | **185个接口全覆盖** | **~191个用例** |

## 运行前提
1. 确保阴道镜系统已启动（https://127.0.0.1:7002）
2. 已安装依赖：`pip install pytest requests`

## 运行命令

### 运行全部
```
python -m pytest E:\数据监控分析\colposcope_tests\ -v
```

### 运行单个文件
```
python -m pytest E:\数据监控分析\colposcope_tests\test_01_login.py -v
```

### 生成HTML报告
```
pip install pytest-html
python -m pytest E:\数据监控分析\colposcope_tests\ -v --html=test_report.html
```
