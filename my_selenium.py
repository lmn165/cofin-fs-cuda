from bs4 import BeautifulSoup
from selenium import webdriver
# import unittest
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.common.keys import Keys

path = 'C:\\Users\\bitcamp\\ai-work\\flaskProject\\data'
chromedriver = 'C:\\Users\\bitcamp\\ai-work\\flaskProject\\data\\chromedriver.exe'


class MySelenium(object):
    def __init__(self):

        self.driver = webdriver.Chrome(chromedriver)

    def naver_login(self):
        driver = self.driver
        driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        driver.implicitly_wait(3)
        driver.find_element_by_id('id_line').send_keys('coolbeat')
        driver.find_element_by_id('pw_line').send_keys('password')
        driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        driver.implicitly_wait(3)
        # driver.find_element_by_link_text('검색').click()

    def scolkg(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.get('https://scolkg.com/')
        driver.implicitly_wait(time_to_wait=5)
        element = driver.find_element_by_xpath('//*[@id="app_coinboard"]/div[2]/table/tbody/tr[8]/td[6]').text
        print('---------------')
        print(element)
        driver.quit()

    def instar(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        try:
            driver.find_element_by_name('username').send_keys('USERNAME')
            time.sleep(5)
            driver.find_element_by_name('password').send_keys('PASSWORD')
            time.sleep(5)
            insta_login_btn = '.sqdOP.L3NKy.y3zKF     '
            driver.find_element_by_css_selector(insta_login_btn).click()
            is_login_success = True
            print('성공')
        except:
            print('login FAIL')
            is_login_success = False

    def google(self):
        driver = self.driver
        driver.get('https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl')
        # search tag using id
        elem = driver.find_element_by_name('q').send_keys('python')
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(time_to_wait=10)
        driver.close()

    def naver_movie(self):
        driver = self.driver
        driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_divs = soup.find_all('div', attrs={'class', 'tit3'})
        products = [[div.a.string for div in all_divs]]
        with open(f'{path}naver_movie_dataset.csv', 'w', newline='', encoding='UTF-8') as f:
            wr = csv.writer(f)
            wr.writerows(products)
        driver.close()


if __name__ == '__main__':
    sel = MySelenium()
    # sel.scolkg()
    sel.google()
    # sel.naver_movie()
