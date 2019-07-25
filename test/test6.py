import urllib.request
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    req.add_header('Referer',
                   'http://ip.zdaye.com/dayProxy.html')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html


def get_img(html):
    # 匹配规则 (?: 不匹配(  [0,1]?\d?\d|2[0-4]\d|25[0-5] 匹配如：112，245，1，2
    # \:\d{4}  这个匹配 ：加四个数字也就是端口
    # [0,1]?  ？代表前面那个可有可无
    p = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\D+?(?:6[0-5]{2}[0-3][0-5]|[1-5]\d{4}|[1-9]\d{1,3}|[0-9])\b"
    iplist = re.findall(p, html)

    for each in iplist:
        print(each)


if __name__ == "__main__":
    url = "http://ip.zdaye.com/dayProxy/ip/314208.html"
    get_img(open_url(url))
