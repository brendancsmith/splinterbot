#------------------------------ imports --------------------------------

# standard modules
import types

# intra-project modules
import utils

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
        self._extend_driver(driver)  # must be before wrap
        self._wrap_driver(driver)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.__exit__(exc_type, exc_value, traceback)

    @staticmethod
    def _extend_driver(driver):
        def find_by_text(self, text):
            return self.find_by_xpath("//*[text()='%s']" % text)

        driver.find_by_text = types.MethodType(find_by_text, driver)

    def _wrap_driver(self, driver):
        # add instance methods that fall through to the driver
        for methodName in self._fallThrough:
            def wrapped_method(self):
                return self.driver.__getattribute__(methodName)()

            self.__dict__[methodName] = types.MethodType(wrapped_method, self)


class FrameBrowser(Browser):

    def __init__(self, driver, frameName):
        super(FrameBrowser, self).__init__(driver)

        self.driver.driver.switch_to.frame(frameName)

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.driver.switch_to.frame(None)


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
        accountOptions = self.option_values_of_select(accountPicker)

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

    @staticmethod
    def option_values_of_select(selectEl):
        """Retrieves the value attributes of the option nodes within a
        select tag"""

        optionEls = selectEl.find_by_tag('option')
        optionValues = [el.value for el in optionEls]

        return optionValues


class MyREDBrowser(Browser):
    """A Splinter web driver wrapper for UNL MyRED."""

    domain = 'myred.unl.edu'

    def login(self, username, password):
        self.driver.fill('userid', username)
        self.driver.fill('pwd', password)

        buttonLogIn = self.driver.find_by_css('.submit') \
                                 .find_by_tag('input')
        buttonLogIn.click()

    def nav_home(self):
        self.driver.visit('http://' + self.domain)

    def nav_to_enrollment_planner(self):
        # open the enrollment navbar element
        enrollmentMenu = self.driver.find_by_id('menu-item-1-1')
        enrollmentMenu.mouse_over()

        # click the Enrollment Planner menu option
        buttonEnrollmentPlanner = self.driver.find_by_id('menu-item-1-3-1')
        while not buttonEnrollmentPlanner.visible:
            utils.wait(1)
        buttonEnrollmentPlanner.click()

    def get_panel_browser(self):
        return MyREDPanelBrowser(self.driver, 'TargetContent')


class MyREDPanelBrowser(FrameBrowser):

    def nav_to_shopping_cart(self):
        # click the shopping cart tab in the enrollment panel
        self.driver.click_link_by_text('shopping cart')

    def choose_spring_semester(self):
        # id = 'SSR_DUMMY_RECV1$sels$1$$0'
        springRadioButton = self.driver.find_by_id('SSR_DUMMY_RECV1$sels$1$$0')
        springRadioButton.check()

        continueButton = self.driver.find_by_id('DERIVED_SSS_SCT_SSR_PB_GO')
        continueButton.click()

    def check_class_status(self):
        statusIcon = self.driver.find_by_id(
            'win1divDERIVED_REGFRM1_SSR_STATUS_LONG$0')
        
        status = statusIcon.find_by_tag('img')['alt']
        return status
