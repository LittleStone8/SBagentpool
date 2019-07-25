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
        options.add_argument('disable-infobars')
        #options.add_argument("--headless")
        proxy='122.136.212.132:53281'
        #options.add_argument('--proxy-server=http://%s' % proxy)
        browser = webdriver.Chrome(options = options)
        browser.set_page_load_timeout(60)
        browser.set_script_timeout(60)  # 这两种设置都进行才有效
        #browser = webdriver.Chrome()
        browser.implicitly_wait(60)
        proxy_list = set()
        ss=acw_tc='781bad0615628588595956635e7e643c2cc65c26f7efa773ed1ad52c15b626; __guid=12269292.2328128639945778700.1562859192807.8; ASPSESSIONIDAAAQDBAC=AHNJPFCAPAHFIOPCBENCOMNF; __51cke__=; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1563973333,1563973335,1563973343,1563973356; monitor_count=25; __tins__16949115=%7B%22sid%22%3A%201563975387974%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201563977202686%7D; __51laig__=7; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1563975403'

        browser.add_cookie()
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
url_xpath_kuaidaili = '//*[@id="list"]/table/tbody/tr[position()>1]'
url_xpath_66 = '//*[@id="footer"]/div/table/tbody/tr[position()>1]'
pool = ThreadPool(10)
for m in range(1, 2):
    url_kuaidaili = 'http://www.kuaidaili.com/free/inha/%s' % (m)
    #url_66 = 'http://www.66ip.cn/areaindex_%s/1.html' % (m)
    daye_url='http://ip.zdaye.com/dayProxy/ip/314188.html'
    url_66='http://www.66ip.cn/areaindex_6/1.html'
    #results = get_proxy_list(url_66, url_xpath_66)
    pool.run(func=get_proxy_list, args=(daye_url, url_xpath_kuaidaili,))
    print(11)
    # 停0.5s再抓取
