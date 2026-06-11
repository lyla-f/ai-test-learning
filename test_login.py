import requests
import warnings
warnings.filterwarnings("ignore")

def test_login_success():
	url = "https://127.0.0.1:7002/api/common/login"
	data = {
		"username": "admin",
		"password":"FsKgVFHIqn5oc2J2eqaxjg=="
	}
	response =requests.post(url, json=data, verify=False)
	result = response.json()
	
	assert result["code"] == 200
	assert result["msg"] =="OK"
	print("✅ 登录成功，token已获取")

def test_login_wrong_password():
	url ="https://127.0.0.1:7002/api/common/login"
	data = {
		"username":"admin",
		"username":"wrongpassword"
	}
	response =requests.post(url,json=data,verify=False)
	result =response.json()
	
	assert result["code"] !=200
	print("✅ 错误密码被正确拦截")