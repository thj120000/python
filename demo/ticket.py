from splinter import Browser
from splinter import driver
from splinter.driver import webdriver
from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from time import sleep

login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
index_url = "https://kyfw.12306.cn/otn/view/index.html"
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
user_name = u'thj120000'  #12306账号
password = u'thj52191025' #12306密码


passengers = [u'唐化江']
#fromStation = "%u5317%u4EAC%2CBJP" #北京
#toStation = "%u4E4C%u9C81%u6728%u9F50%u5357%2CWMR" #乌鲁木齐
departDate = "2019-01-19"

fromStation = "%u5E93%u5C14%u52D2%2CKLR" #库尔勒
toStation = "%u91CD%u5E86%u5317%2CCUW" #重庆北


#起点站到终点站的
train_order = [0,1]
mail_host = 'smtp.qq.com'  #邮箱服务器
sender = '2464237217@qq.com' #发送方邮箱
pwd = ''  #发送方密码

receivers = '2464237217@qq.com' #接收方

#chromedriver = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
chromedriver = 'C:/others/python3.7/Scripts/chromedriver.exe'
os.environ['webdriver.chrome.driver'] = chromedriver

def login(browser):
    while browser.is_text_present(u'登录'):
        browser.find_by_text(u"账号登录")[0].click()
        sleep(1)
        browser.find_by_id("J-userName").fill(user_name)
        sleep(1)
        browser.find_by_id("J-password").fill(password)
        sleep(1)
        print(u'please input valid code')
        sleep(5)
        browser.click_link_by_id("J-login")
        sleep(1)
        while (True):
            if browser.url != index_url:
                sleep(1)
            else:
                break
        browser.visit(ticket_url)
        sleep(1)
        #通过查询浏览器的cookies信息可知出发地点和目的地点的代号
        browser.cookies.add({"_jc_save_fromStation":fromStation})
        browser.cookies.add({"_jc_save_toStation": toStation})
        browser.cookies.add({"_jc_save_fromDate": departDate})
        browser.reload()
        #选中学生票选项
        #browser.click_link_by_id("sf2")
        #sleep(2)

        # 查询操作直至有可预订的车票
        count = 0
        while browser.url == ticket_url:
            browser.click_link_by_id("query_ticket")
            count += 1
            print("查询次数：%d"%(count))
            sleep(1)
            try:
                #if(len(browser.find_by_text(u"预订")) > train_order):
                for i in train_order:
                    print(i)
                    browser.find_by_text(u"预订")[i].click()
                    try:
                        browser.find_element_by_xpath("//select[@id='seatType_1']/option[#value=3]").click()
                        break
                    except Exception as e:
                        print("当前车次无卧铺票")
                    # if browser.is_text_present(u'硬卧（￥310.5）有票'):
                    #     break
                    if browser.url == ticket_url:
                        continue
                    else:
                        browser.visit(ticket_url)
                        browser.cookies.add({"_jc_save_fromStation": fromStation})
                        browser.cookies.add({"_jc_save_toStation": toStation})
                        browser.cookies.add({"_jc_save_fromDate": departDate})
                        browser.reload()
            except Exception as e:
                print(e)
                print("当前车次无可预订车票")
                continue
        # 开始订票
        # 添加乘客
        for passenger in passengers:
            browser.find_by_text(passenger)[0].click()
            if browser.is_text_present(u'您是要购买学生票吗'):
                browser.click_link_by_id('dialog_xsertcj_ok')
        #TODO:选择硬座、硬卧等信息
        sleep(1)
        browser.find_by_text(u'提交订单')[0].click()
        if browser.is_text_present(u'请核对以下信息'):
            browser.click_link_by_id('qr_submit_id')
            #browser.find_by_text(u'确认')[0].click()
            if browser.is_text_present(u'请在30分钟内进行支付'):
                message = MIMEText(fromStation + '到' + toStation + '的车票下单成功，请及时支付！', 'plain', 'utf-8')
                message['From'] = Header('python抢票脚本', 'utf-8')
                message['To'] = Header('python抢票脚本', 'utf-8')
                subject = '12306订单已生成'
                message['Subject'] = Header(subject, 'utf-8')

                try:
                    smtpObj = smtplib.SMTP()
                    smtpObj.connect(mail_host, 25)
                    smtpObj.login(sender, pwd)
                    smtpObj.sendmail(sender, receivers, message.as_string())
                    print('邮件已发送至' + receivers)
                except smtplib.SMTPException:
                    print('发送邮件失败')

        while(True):
            sleep(1)

def getTickt():
    browser = Browser(driver_name='chrome')
    # 打开的浏览器窗口要足够大，不然程序崩溃，不过
    # browser.full_screen()似乎不起作用
    windows_size = browser.driver.get_window_size()
    print(windows_size)
    browser.driver.set_window_size(height=windows_size["height"], width=windows_size["width"]*2)
    browser.visit(login_url)
    login(browser)

if __name__ == '__main__':
    getTickt()