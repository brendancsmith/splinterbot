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

        buttonSignon = self.find_by_id('btnSignon')
        buttonSignon.click()

    def find_account_links(self):
        return self.find_by_css('a.account')

    def nav_home(self):
        self.visit('https://online.wellsfargo.com/das/cgi-bin/session.cgi'
                   '?screenid=SIGNON_PORTAL_PAUSE')

    def nav_to_download_page(self):
        self.nav_home()
        self.click_link_by_text('Account Activity')
        self.click_link_by_text('Download Activity')

    def download_selected_account(self):
        # must be on download page
        
        self.choose('fileFormat', 'quickenOfx')

        buttonDownload = self.find_by_id('buttonPrimary').find_by_tag('input')
        buttonDownload.click()
