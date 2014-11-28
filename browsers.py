from splinter.driver.webdriver.firefox import WebDriver as FirefoxWebDriver


class WFBrowser(FirefoxWebDriver):

    def login(self, username, password):
        raise NotImplementedError()
