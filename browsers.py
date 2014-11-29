#------------------------------ imports --------------------------------

# standard modules
# N/A

# intra-project modules
# N/A

# external libraries
from splinter.driver.webdriver.firefox import WebDriver as FirefoxWebDriver

#-----------------------------------------------------------------------


class WFBrowser(FirefoxWebDriver):

    url = 'http://wellsfargo.com'

    def login(self, username, password):
        self.fill('userid', username)
        self.fill('password', password)

        btnSignon = self.find_by_id('btnSignon')
        btnSignon.click()

    def find_account_links(self):
        return self.find_by_css('a.account')

    def nav_to_download_page(self):
        self.click_link_by_text('Account Activity')
        self.click_link_by_text('Download Activity')
