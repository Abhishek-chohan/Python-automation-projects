from selenium import webdriver
from time import sleep
user=input("Enter your Username/E-mail : ")
paswd=input("Enter Password : ")


class IGBOT:
    def __init__(self, user, paswd):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(user)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(paswd)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
        sleep(4)
        li1 = self.get_followers()
        sleep(4)
        li2 = self.get_following()
        sleep(4)
        li3 = [name for name in li2 if name not in li1]
        print(li3)

    def get_followers(self):
       self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
       sleep(2)
       self.scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
       last_ht, ht = 0, 1
       while last_ht != ht:
           last_ht = ht
           sleep(1)
           ht = self.driver.execute_script(
               """arguments[0].scrollTo(0,arguments[0].scrollHeight);return arefguments[0].scrollHeight;""",
               self.scroll_box)
       links = self.scroll_box.find_elements_by_tag_name('a')
       names = []
       for name in links:
           if name.text != '':
               names.append(name.text)
       sleep(1)
       self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()

       return names


    def get_following(self):
       self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
       sleep(2)
       self.scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
       last_ht, ht = 0, 1
       while last_ht != ht:
           last_ht = ht
           sleep(1)
           ht = self.driver.execute_script(
               """arguments[0].scrollTo(0,arguments[0].scrollHeight);return arguments[0].scrollHeight;""",
               self.scroll_box)
       links = self.scroll_box.find_elements_by_tag_name('a')

       names = []
       for name in links:
           if name.text != '':
               names.append(name.text)

       sleep(1)

       self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()

       return names



IGBOT(user,paswd)

