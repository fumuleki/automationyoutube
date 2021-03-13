from selenium import webdriver


class Music():
    def _init_(self):
        self.driver = webdriver.chrome()

    def play(self):
        name = input("enter a youtube channel name")
        self.driver.get("https://www.youtube.com/user/fallyipupa/videos")
        new = self.driver.find_element_by_xpath('//*[@id="channel-name"]')
        new.click()


bot = Music()
bot.play()
