import re
import time
from email._header_value_parser import get_attribute
from telnetlib import EC

from selenium import webdriver

# browser = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from scheduler.threadpool import ThreadPool


def get_proxy_list(url, url_xpath):
    '''
        返回抓取到代理的列表
        整个爬虫的关键
        '''
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    # options.add_argument("--headless")
    proxy = '122.136.212.132:53281'

    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    options.add_experimental_option('prefs', prefs)
    # options.add_argument('--proxy-server=http://%s' % proxy)
    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(60)
    browser.set_script_timeout(60)  # 这两种设置都进行才有效
    # browser.add_cookie()
    # browser = webdriver.Chrome()
    browser.implicitly_wait(60)
    proxy_list = set()
    browser.get(url)
    sdasda = browser.get_cookies()

    # assss=browser.find_elements_by_tag_name("a")
    # sum=0
    # for a in assss:

    #   ss=str(a.get_attribute('href'))
    #   sum=sum+1
    #   print(ss+str(sum))
    #   if ss=='http://ip.zdaye.com/dayProxy/ip/314191.html':
    #       a.click()
    # print(sum)
    # time.sleep(10)
    element = browser.find_elements_by_xpath(
        '//*[@id="J_posts_list"]//div[@class="thread_item"]//div[@class="thread_content"]//h3[@class="thread_title"]//a')
    print(element)
    element[0].click()
    time.sleep(1)

    elementw = browser.find_elements_by_xpath('//div[@class="cont"]')
    print(elementw[0].text)


    p = r'(?:((?:\d|[1-9]\d|1\d{2}|2[0-5][0-5])\.(?:\d|[1-9]\d|1\d{2}|2[0-5][0-5])\.(?:\d|[1-9]\d|1\d{2}|2[0-5][0-5])\.(?:\d|[1-9]\d|1\d{2}|2[0-5][0-5]))\D+?(6[0-5]{2}[0-3][0-5]|[1-5]\d{4}|[1-9]\d{1,3}|[0-9]))'
    #result = re.findall(p, elementw[0].text)
    result = re.findall(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\D+?(?:6[0-5]{2}[0-3][0-5]|[1-5]\d{4}|[1-9]\d{1,3}|[0-9])\b", elementw[0].text)
    print(result)
    for results in result:
        print(results)
    # element.click(); # click方法点击目标元素thread_title
    ''''
    browser2 = webdriver.Chrome(options=options)
    browser2.delete_all_cookies()
    browser2.set_page_load_timeout(60)
    browser2.set_script_timeout(60)  # 这两种设置都进行才有效
    #browser.add_cookie()
    #browser = webdriver.Chrome()
    browser2.implicitly_wait(60)
    cookiessss={}

    for item in sdasda:
        cookiessss[item['name']] = item['value']
    print(3333)
    print(cookiessss)


    for cookie in cookiessss:
        print(cookie)
        browser2.add_cookie({
            "domain": "ip.zdaye.com",
            "name": cookie,
            "value": cookiessss[cookie]
        })
    for c in sdasda:
        new = dict(c, **{
        })
    browser2.add_cookie(new)

    for item in sdasda:
        print(item)
        browser2.add_cookie(item)
    #print(cookiessss)

    for cookie in sdasda:
        print(cookie)
        browser2.add_cookie({
            "domain": "ip.zdaye.com",
            "name": cookie,
            "value": sdasda[cookie],
            "path": '/',
            "expires": None
        })
    '''''
    #browser.get('http://ip.zdaye.com/dayProxy/ip/237313.html')

    # WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, url_xpath_66)))
    print('3333333')
    # 找到代理table的位置
    elements = browser.find_elements_by_xpath(url_xpath)
    for element in elements:
        ip = element.find_element_by_xpath('./td[1]').text
        port = element.find_element_by_xpath('./td[2]').text
        ip_addr = ip + ':' + port
        print(ip_addr)
        proxy_list.add(ip_addr)
    # browser.quit()
    print('运行结束' + str(len(proxy_list)))
    return proxy_list


pass

url_xpath_66 = '//*[@id="footer"]/div/table/tbody/tr[position()>1]'
url_xpath_66 = '//*[@id="threadblock_list"]/div/table/tbody/tr[position()>1]'
url_xpath_kuaidaili = '//*[@id="list"]/table/tbody/tr[position()>1]'
daye = '//*[@id="cont"]/br'
pool = ThreadPool(10)

for m in range(1, 2):
    # url_66 = 'http://www.66ip.cn/areaindex_%s/1.html' % (m)
    url_66 = 'http://www.66ip.cn/areaindex_6/1.html'
    # daye_url='http://ip.zdaye.com/dayProxy/ip/237313.html'
    daye_url = 'http://ip.zdaye.com/dayProxy/2019/7/1.html'
    # results = get_proxy_list(url_66, url_xpath_66)
    pool.run(func=get_proxy_list, args=(daye_url, daye,))
    print(11)
    # 停0.5s再抓取
