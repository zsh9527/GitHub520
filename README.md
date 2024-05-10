# GitHub520

## 功能
github的CDN被某墙屏了，由于网络代理商的原因，所以访问下载很慢  
该项目用于通过APi解析github相关域名对应ip, 并修改hosts文件


## 二、使用方法

### 2.1 复制下面的内容
```bash
# GitHub520 Host Start
140.82.112.26                 alive.github.com
140.82.114.25                 live.github.com
185.199.108.154               github.githubassets.com
140.82.114.21                 central.github.com
185.199.108.133               desktop.githubusercontent.com
185.199.108.153               assets-cdn.github.com
185.199.108.133               camo.githubusercontent.com
185.199.108.133               github.map.fastly.net
199.232.69.194                github.global.ssl.fastly.net
140.82.113.4                  gist.github.com
185.199.108.153               github.io
140.82.114.3                  github.com
192.0.66.2                    github.blog
140.82.112.6                  api.github.com
185.199.108.133               raw.githubusercontent.com
185.199.108.133               user-images.githubusercontent.com
185.199.108.133               favicons.githubusercontent.com
185.199.108.133               avatars5.githubusercontent.com
185.199.108.133               avatars4.githubusercontent.com
185.199.108.133               avatars3.githubusercontent.com
185.199.108.133               avatars2.githubusercontent.com
185.199.108.133               avatars1.githubusercontent.com
185.199.108.133               avatars0.githubusercontent.com
185.199.108.133               avatars.githubusercontent.com
140.82.113.10                 codeload.github.com
52.217.139.169                github-cloud.s3.amazonaws.com
52.217.93.28                  github-com.s3.amazonaws.com
52.216.153.172                github-production-release-asset-2e65be.s3.amazonaws.com
52.217.199.249                github-production-user-asset-6210df.s3.amazonaws.com
52.217.200.1                  github-production-repository-file-5c1aeb.s3.amazonaws.com
185.199.108.153               githubstatus.com
64.71.144.202                 github.community
23.100.27.125                 github.dev
185.199.108.133               media.githubusercontent.com
185.199.108.133               cloud.githubusercontent.com
185.199.108.133               objects.githubusercontent.com


# Update time: 2022-01-01T10:38:20+08:00
# Update url: https://raw.hellogithub.com/hosts
# Star me: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End

```

### 2.1 手动方式

#### 2.1.1 修改 hosts 文件
hosts 文件在每个系统的位置不一，详情如下：
- Windows 系统：`C:\Windows\System32\drivers\etc\hosts`
- Linux 系统：`/etc/hosts`
- Mac（苹果电脑）系统：`/etc/hosts`
- Android（安卓）系统：`/system/etc/hosts`
- iPhone（iOS）系统：`/etc/hosts`

#### 2.1.2 激活生效
大部分情况下是直接生效，如未生效可尝试下面的办法，刷新 DNS：

1. Windows：在 CMD 窗口输入：`ipconfig /flushdns`

2. Linux 命令：`sudo nscd restart`，如报错则须安装：`sudo apt install nscd` 或 `sudo /etc/init.d/nscd restart`

3. Mac 命令：`sudo killall -HUP mDNSResponder`

## TODO
- [x] 定时自动更新 hosts 内容
- [x] hosts 内容无变动不会更新
- [ ] 寻到最优 IP 解析结果
- [ ] 多线程