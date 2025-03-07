import sys, os
# 设置代理环境变量
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:8888'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:8888'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lanzou.api import LanZouCloud
import time
lzy = LanZouCloud()
cookie = {'ylogin': '3778427', 'phpdisk_info': 'AjUDNlI3AzcGMFU3WzZaCQdlVmZbCwdhATEAYwI8Cz5YZF5qDGcCPQM5BGJaCQRvVGZQYF4wAjcOOlczUDcKPQI%2FAzhSZQM7BjNVZFtgWmEHM1ZlWzIHZgFhAGUCNAtvWG9eaww8Aj4DNQRtWmMEV1Q1UGFeNAJtDjpXP1BgCjECNQM5UjY%3D'}
print(lzy.login_by_cookie(cookie) == LanZouCloud.SUCCESS)
def get_dir_list():
    
    dirs = lzy.get_dir_list()
    print(dirs)
def get_folder_info_by_id():
    code = lzy.get_folder_info_by_id("9522903")
    print(code)
    
def get_durl_by_id():
    code = lzy.get_durl_by_id(226574157)
    print(code)
    
def get_share_info():
    code = lzy.get_share_info(226574157)
    print(code)

def get_durl_by_url():
    code = lzy.get_durl_by_url('https://wwpk.lanzoup.com/itDr22pv7vna')
    print(code)
    
def upload_file():
    def handler(fid, is_file):
        print(fid, is_file)
    file = open(r"D:\CODE\VsCode_CODE\Python\lanzouapi\LanZouCloud-API\test\test2.py", 'rb')
    code= lzy.upload_binary_file("qqq.txt", file, -1, uploaded_handler=handler)
    print(code)
    
if __name__ == "__main__":
    get_durl_by_id()