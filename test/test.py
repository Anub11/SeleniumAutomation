import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class TheSparksFoundation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("..\drivers\chromedriver.exe")
        cls.driver.maximize_window()

    def test_main_page(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org")

    
        self.assertIn("The Sparks Foundation", driver.title)
        print("Test 1 Completed.....")

        
        logo = driver.find_element_by_css_selector("a.col-md-6 > img:nth-child(1)")
        logo.is_displayed()
        print("Test 2 Completed....")
        
        navbar = driver.find_element_by_tag_name("nav")
        navbar.is_displayed()
        print("Test 3 Completed....")


        a=self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/a')
        a.click()
        time.sleep(6)
        print("Test 4 Completed....")

        b = self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/a')
        b.click()
        time.sleep(6)
        print("Test 5 Completed....")

        c = self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a')
        c.click()
        time.sleep(6)
        print("Test 6 Completed....")

        d=self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/ul/li[2]/a')
        d.click()
        time.sleep(6)
        print("Test 7 Completed....")


        self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[2]/a').click()
        time.sleep(4)
        print("Test 8 Completed....")
        self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[2]/ul/li[5]/a').click()
        time.sleep(6)
        print("Test 9 Completed....")

        self.driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[6]/a').click()
        time.sleep(4)
        print("Test 10 Completed....")
        





    def test_join_us_page(self):

        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/join-us/why-join-us/")

        name = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]"
        )
        role = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/form/select"
        )

        contact = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]"
        )

        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", name)
        time.sleep(1)

        name.send_keys("Anubhav Bej")
        time.sleep(1)

        contact.send_keys("anub@xyz.in")
        time.sleep(1)

        drp = Select(role)


        drp.select_by_visible_text("Student")

        print("Test 11 Completed....")
        time.sleep(1)




    @classmethod
    def tearDownClass(cls):
        
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
