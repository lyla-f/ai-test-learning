import requests
import warnings
warnings.filterwarnings("ignore")

def login(username,password):
	url = "https://127.0.0.1:7002/api/common/login"
	data = {
		"username": username,
		"password": password
	}
	response =requests.post(url, json=data, verify=False)
	return response.json()
	
def test_login_success():
	result = login("admin","FsKgVFHIqn5oc2J2eqaxjg==")
	assert result["code"] == 200
	assert result["msg"] =="OK"
	print("✅ 登录成功")

def test_login_wrong_password():
	result = login("admin","wrongpassword")
	assert result["code"] !=200
	print("✅ 错误密码被正确拦截")