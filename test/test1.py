import time
from telnetlib import EC

from selenium import webdriver



#browser = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from scheduler.threadpool import ThreadPool


def get_proxy_list(url,url_xpath):
        '''
        返回抓取到代理的列表
        整个爬虫的关键
        '''


        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', prefs)
        options.add_argument('disable-infobars')


        #options.add_argument('referer="http://ip.zdaye.com/dayProxy.html"')
        options.add_argument('lang=zh_CN.UTF-8')
        #options.add_argument('--referer=http://ip.zdaye.com/dayProxy.html')
        options.add_argument('Referer=http://ip.zdaye.com/dayProxy.html')
        #options.add_argument("--headless")

        proxy='122.136.212.132:53281'
        #options.add_argument('--proxy-server=http://%s' % proxy)
        browser = webdriver.Chrome(options = options)
        browser.set_page_load_timeout(60)
        browser.set_script_timeout(60)  # 这两种设置都进行才有效
        #browser = webdriver.Chrome()
        browser.implicitly_wait(60)
        proxy_list = set()
        browser.get(url)
        #WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, url_xpath_66)))
        print('3333333')
        # 找到代理table的位置
        elements = browser.find_elements_by_xpath(url_xpath)
        for element in elements:
            ip = element.find_element_by_xpath('./td[1]').text
            port = element.find_element_by_xpath('./td[2]').text
            ip_addr=ip+':' +port
            print(ip_addr)
            proxy_list.add(ip_addr)
        #browser.quit()
        print('运行结束'+str(len(proxy_list)))
        return proxy_list
pass

url_xpath_66 = '//*[@id="footer"]/div/table/tbody/tr[position()>1]'
url_xpath_66 = '//*[@id="footer"]/div/table/tbody/tr[position()>1]'
url_xpath_kuaidaili = '//*[@id="list"]/table/tbody/tr[position()>1]'
daye = '//*[@id="cont"]/br'
pool = ThreadPool(10)
for m in range(1, 2):
    #url_66 = 'http://www.66ip.cn/areaindex_%s/1.html' % (m)
    url_66='http://www.66ip.cn/areaindex_6/1.html'
    #daye_url='http://ip.zdaye.com/dayProxy/ip/237313.html'
    #results = get_proxy_list(url_66, url_xpath_66)
    pool.run(func=get_proxy_list, args=('http://ip.zdaye.com/dayProxy.html', daye,))
    print(11)
    # 停0.5s再抓取
