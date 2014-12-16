#------------------------------ imports --------------------------------

# standard modules
import types

# intra-project modules
# N/A

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
