#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   2020-05-19 15:27
#   Desc    :   获取最新的 GitHub 相关域名对应 IP
import os
import re
import json
import threading

from datetime import datetime, timezone, timedelta
from collections import Counter

import requests
from retry import retry

# 需要查询域名
domainList = [
    "alive.github.com",
    "live.github.com",
    "github.githubassets.com",
    "central.github.com",
    "desktop.githubusercontent.com",
    "assets-cdn.github.com",
    "camo.githubusercontent.com",
    "github.map.fastly.net",
    "github.global.ssl.fastly.net",
    "gist.github.com",
    "github.io",
    "github.com",
    "github.blog",
    "api.github.com",
    "raw.githubusercontent.com",
    "user-images.githubusercontent.com",
    "favicons.githubusercontent.com",
    "avatars5.githubusercontent.com",
    "avatars4.githubusercontent.com",
    "avatars3.githubusercontent.com",
    "avatars2.githubusercontent.com",
    "avatars1.githubusercontent.com",
    "avatars0.githubusercontent.com",
    "avatars.githubusercontent.com",
    "codeload.github.com",
    "github-cloud.s3.amazonaws.com",
    "github-com.s3.amazonaws.com",
    "github-production-release-asset-2e65be.s3.amazonaws.com",
    "github-production-user-asset-6210df.s3.amazonaws.com",
    "github-production-repository-file-5c1aeb.s3.amazonaws.com",
    "githubstatus.com",
    "github.community",
    "github.dev",
    "media.githubusercontent.com",
    "cloud.githubusercontent.com",
    "objects.githubusercontent.com"
]

IPADDRESS_PREFIX = ".ipaddress.com"

content_list = []

# utf-8编码格式打开文件
def open_with_utf8(filename, model):
    return open(filename, model, -1, "utf8")

# 写入host文件
def write_host_file():
    time = datetime.utcnow().astimezone(
        timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()
    commit = "# 文件路径 ‪C:/Windows/System32/drivers/etc/hosts \n"
    commit += "# 刷新DNS ipconfig /flushdns \n"
    commit += "# github host  -- " + str(time) + "\n"
    output_file_path = os.path.join(os.path.dirname(__file__), 'hosts')
    with open_with_utf8(output_file_path, "w") as output_fb:
        output_fb.write(commit)
        for obj in content_list:
            output_fb.write(obj[1].ljust(30) + obj[0] + "\n")

# 写入json文件, 可用于判断是否变化
def write_json_file():
    output_file_path = os.path.join(os.path.dirname(__file__), 'hosts.json')
    with open_with_utf8(output_file_path, "w") as output_fb:
        json.dump(content_list, output_fb)


#  生成查询ipaddress的url
def make_ipaddress_url(domain: str):
    dot_count = domain.count(".")
    if dot_count > 1:
        raw_url_list = domain.split(".")
        tmp_url = raw_url_list[-2] + "." + raw_url_list[-1]
        ipaddress_url = "https://" + tmp_url + IPADDRESS_PREFIX + "/" + domain
    else:
        ipaddress_url = "https://" + domain + IPADDRESS_PREFIX
    return ipaddress_url


# 查询域名对应ip
@retry(tries=3)
def findIpaddress(session: requests.session, domain: str):
    url = make_ipaddress_url(domain)
    try:
        rs = session.get(url, timeout=5)
        pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
        ip_list = re.findall(pattern, rs.text)
        ip_counter_obj = Counter(ip_list).most_common(1)
        if ip_counter_obj:
            content_list.append([domain, ip_counter_obj[0][0]])
        raise Exception("ip address empty")
    except Exception:
        failed = 1

# 请求线程
class RequestThread(threading.Thread):
    def __init__(self, domain):
        threading.Thread.__init__(self)
        self.domain = domain

    def run(self):
        session = requests.session()
        findIpaddress(session, self.domain)

def main():
    threads = []
    for domain in domainList:
        thread = RequestThread(domain)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

    if len(content_list) != 0:
        print("查询成功%d, 查询失败%d" % (len(content_list), len(domainList) - len(content_list)))
        write_json_file()
        write_host_file()
    else:
        print("全部查询失败")

if __name__ == '__main__':
    main()
