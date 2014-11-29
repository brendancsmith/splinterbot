#------------------------------ imports --------------------------------

# standard modules
# N/A

# intra-project modules
# N/A

# external libraries
from splinter.driver.webdriver.firefox import WebDriver as FirefoxWebDriver

#-----------------------------------------------------------------------


class WFBrowser(object):
    """A wrapper for a Splinter web driver, used for specific
    Wells Fargo actions. Ideally, some general driver methods should
    fall through to be accessible by the browser interface."""

    domain = 'wellsfargo.com'

    def __init__(self):
        self.driver = FirefoxWebDriver()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.__exit__(exc_type, exc_value, traceback)

    def login(self, username, password):
        self.driver.fill('userid', username)
        self.driver.fill('password', password)

        buttonSignon = self.driver.find_by_id('btnSignon')
        buttonSignon.click()

    def find_account_links(self):
        return self.driver.find_by_css('a.account')

    def nav_home(self):
        if not self.domain in self.driver.url:
            self.driver.visit('http://' + self.domain)
        else:
            self.driver.visit('https://online.wellsfargo.com/'
                              'das/cgi-bin/session.cgi'
                              '?screenid=SIGNON_PORTAL_PAUSE')

    def nav_to_download_page(self):
        self.nav_home()
        self.driver.click_link_by_text('Account Activity')
        self.driver.click_link_by_text('Download Activity')

    def download_selected_account(self):
        # must be on download page

        self.driver.choose('fileFormat', 'quickenOfx')

        buttonDownload = self.driver.find_by_id('buttonPrimary') \
                                    .find_by_tag('input')
        buttonDownload.click()
