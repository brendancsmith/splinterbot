#------------------------------ imports --------------------------------

# standard modules
# N/A

# intra-project modules
from splinterbot.browsers import Browser, FrameBrowser

# external libraries
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#-----------------------------------------------------------------------


class MyRedBrowser(Browser):
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

        WebDriverWait(self.driver.driver, 10).until(
            expected_conditions.visibility_of(buttonEnrollmentPlanner._element)
        )
        buttonEnrollmentPlanner.click()

    def get_panel_browser(self):
        return MyREDPanelBrowser(self.driver, 'TargetContent')


class MyREDPanelBrowser(FrameBrowser):

    def nav_to_shopping_cart(self):
        # click the shopping cart tab in the enrollment panel
        self.driver.click_link_by_text('shopping cart')

    def choose_semester(self, index):
        '''Choose a semester for the shopping cart and click Continue.
        The first semester in the list, which should be the current
        semeseter, will have an index of 0.'''

        semesterRadioId = 'SSR_DUMMY_RECV1$sels${0}$$0'.format(index)

        # id = 'SSR_DUMMY_RECV1$sels$1$$0'
        semesterRadio = self.driver.find_by_id(semesterRadioId)
        semesterRadio.check()

        continueButton = self.driver.find_by_id('DERIVED_SSS_SCT_SSR_PB_GO')
        continueButton.click()

    def parse_shopping_cart(self):
        # must be on shopping cart tab

        cartTable = self.driver.find_by_id('SSR_REGFORM_VW$scroll$0').first

        # filter rows that aren't classes
        def isRowAClass(row):
            return 'trSSR_REGFORM_VW$0' in row['id']
        cartClasses = [row for row in cartTable.find_by_tag('tr')
                       if isRowAClass(row)]

        classes = []
        for i, cartClass in enumerate(cartClasses):

            # grab the name of the class
            nameId = 'win1divP_CLASS_NAME${0}'.format(i)
            className = cartClass.find_by_id(nameId).first.text
            className = className.replace('\n', ' ')

            # grab the open/closed status of the class
            statusId = 'win1divDERIVED_REGFRM1_SSR_STATUS_LONG${0}'.format(i)
            classStatus = cartClass.find_by_id(statusId)\
                                   .find_by_tag('img')['alt']

            classes.append((className, classStatus))

        return classes
