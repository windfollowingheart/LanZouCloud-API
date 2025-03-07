import requests,os
# 创建会话对象
_session = requests.Session()

# 配置代理
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:8888'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:8888'
# _session.proxies = proxies
print(f"当前设置的代理: {_session.proxies}")
# 发起请求
try:
    response = _session.get('http://www.baidu.com')
    print(response.text)
except requests.RequestException as e:
    print(f"请求出错: {e}")