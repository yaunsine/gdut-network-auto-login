"""
    author: yaunsine
    date: 2024/03/15
    content: 校园网登录
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from configparser import ConfigParser
import datetime
import time
import schedule

config = ConfigParser()
config.read("config/myConfig.ini", encoding="utf-8")

username = config['account']['username']
password = config['account']['password']
driver_path = config['drivers']['driverPath']

print(username)
print(password)
print(driver_path)


def login_gdut():
    # 设置无头
    opt = ChromeOptions()
    opt.add_argument('--headless=new')
    # 设置Chrome驱动器的路径
    # 创建一个Chrome WebDriver实例
    driver_service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=driver_service, options=opt)

    net_url = "http://10.0.3.2/a79.htm?wlanuserip=10.43.254.14&wlanacname=&wlanacip=172.16.254.2"
    # 打开网站
    driver.get(net_url)
    # f1.DDDDD
    # f1.upass
    # f1.0MKKey
    try:
        # 输入用户名和密码
        myForm = driver.find_element(By.NAME, "f1")
        username_input = myForm.find_element(By.NAME, "DDDDD")
        password_input = myForm.find_element(By.NAME, "upass")

        username_input.send_keys(username)
        password_input.send_keys(password)

        # 找到并点击登录按钮
        login_button = myForm.find_element(By.NAME, "0MKKey")
        driver.execute_script("arguments[0].click();", login_button)
        # login_button.click()

        print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"))
        print("登录成功.")

    except Exception as e:
        print("Error:", e)

    finally:
        # 关闭浏览器
        driver.quit()


if __name__ == '__main__':
    job = login_gdut

    schedule.every().day.at("06:30").do(job)
    print("已启动任务...")
    while True:
        schedule.run_pending()
        # 为了减轻CPU负担，可以适当地休眠一段时间
        time.sleep(1)
