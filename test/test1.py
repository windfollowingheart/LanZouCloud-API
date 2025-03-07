import sys, os
# 设置代理环境变量
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:8888'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:8888'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lanzou_windfollowingheart.api import LanZouCloud
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
    
def get_durl_by_id(id=226578069):
    code = lzy.get_durl_by_id(id)
    # print(code)
    # print(code.durl)
    return code.durl
    
def get_share_info():
    code = lzy.get_share_info(226574157)
    print(code)

def get_durl_by_url():
    code = lzy.get_durl_by_url('https://wwpk.lanzoup.com/itDr22pv7vna')
    print(code)
    
def upload_file():
    file_id = None
    def handler(fid, is_file):
        nonlocal file_id
        # print(fid, is_file)
        file_id = fid
    # file = open(r"D:\CODE\VsCode_CODE\Python\lanzouapi\LanZouCloud-API\test\test2.py", 'rb')
    file = None
    filename = None
    # file_path = r"D:\123pan\Downloads\csig_issue\文献\基于聚焦堆栈单体数据子集架构的全局成像.pdf"
    file_path = r"D:\CODE\VsCode_CODE\Python\lanzouapi\LanZouCloud-API\test\file.txt"
    last_dot_index = file_path.rfind('.')
    if last_dot_index != -1:
        # 切片拼接完成替换
        filename = file_path[:last_dot_index] + "_" + file_path[last_dot_index + 1:] + ".txt"
        # print(filename)
    with open(file_path, 'rb') as f:
        file = f.read()
    code= lzy.upload_binary_file(filename, file, 11665772, uploaded_handler=handler)
    # print(file_id)
    return file_id
    
if __name__ == "__main__":
    file_id = upload_file()
    print(file_id)
    durl = get_durl_by_id(file_id)
    print(durl)