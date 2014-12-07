#------------------------------ imports --------------------------------

# standard modules
import time
import types

# intra-project modules
import driver_utils

# external libraries
from splinter.driver.webdriver.firefox import WebDriver as FirefoxWebDriver

#-----------------------------------------------------------------------


class Browser(object):
    """A base wrapper for a Splinter web driver, used for page-specific
    actions. General driver methods will fall through to be accessible
    by the browser interface."""

    _fallThrough = ['quit']

    def __init__(self, driver=None):
        if driver is None:
            # Setting FirefoxWebDriver() as a default value for driver
            # causes Firefox to open before user/pass are collected.
            # Not sure why, but we'll just do that here.
            driver = FirefoxWebDriver()

        self.driver = driver
        self._wrap_driver(driver)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.__exit__(exc_type, exc_value, traceback)

    def _wrap_driver(self, driver):
        # add instance methods that fall through to the driver
        for methodName in self._fallThrough:
            def wrapped_method(self):
                return self.driver.__getattribute__(methodName)()

            self.__dict__[methodName] = types.MethodType(wrapped_method, self)

    def wait(self, sec=5):
        time.sleep(sec)


class WFBrowser(Browser):
    """A Splinter web driver wrapper for Wells Fargo."""

    domain = 'wellsfargo.com'

    def login(self, username, password):
        self.driver.fill('userid', username)
        self.driver.fill('password', password)

        buttonSignon = self.driver.find_by_id('btnSignon')
        buttonSignon.click()

    def find_account_links(self):
        """Return a list of links to each account on the home page."""
        # must be on home page
        return self.driver.find_by_css('a.account')

    def nav_home(self):
        """Navigate to the login page if we're not on the domain, and
        the member portal if we are on the domain."""

        if not self.domain in self.driver.url:
            self.driver.visit('http://' + self.domain)
        else:
            self.driver.visit('https://online.wellsfargo.com/'
                              'das/cgi-bin/session.cgi'
                              '?screenid=SIGNON_PORTAL_PAUSE')

    def nav_to_download_page(self):
        """Navigate to the page wherein you can select account activity
        exports."""

        self.nav_home()
        self.driver.click_link_by_text('Account Activity')
        self.driver.click_link_by_text('Download Activity')

    def download_all_accounts(self):
        """Select each available account and download a quicken export"""
        # must be on download page

        # the page refreshes when you select a different account,
        # so we have to find the select element each time
        accountPickerId = 'primaryKey'

        accountPicker = self.driver.find_by_id(accountPickerId)
        accountOptions = driver_utils.option_values_of_select(accountPicker)

        # go through the options on the account drop-down and download them
        for option in accountOptions:
            self.driver.select(accountPickerId, option)
            self.driver.find_by_name('Select').click()
            self.download_selected_account()

    def download_selected_account(self):
        """Download a quicken export for the selected account."""
        # must be on download page

        self.driver.choose('fileFormat', 'quickenOfx')

        buttonDownload = self.driver.find_by_id('buttonPrimary') \
                                    .find_by_tag('input')
        buttonDownload.click()
