#------------------------------ imports --------------------------------

# standard modules
# N/A

# intra-project modules
from gmail import send_email
from splinterbot.bot import Bot, LoginManager
from sites.myred import MyRedBrowser

# external libraries
from splinter.exceptions import ElementDoesNotExist

#-----------------------------------------------------------------------


class EnrollmentChecker(Bot):

    def __init__(self):
        self.logins = LoginManager()

    def run(self):
        """Checks MyRED to see if classes in the shopping cart for next
        semester are open or closed."""

        # get login details from terminal
        self.logins['myred'] = LoginManager.ask('NUID',
                                                'MyRED Password')
        self.logins['gmail'] = LoginManager.ask('Gmail Address',
                                                'Gmail Password')

        # Send a non-error email to verify it's working
        #send_email(gmailAddr, gmailPassword,
        #           'EnrollmentChecker process has started.')

        strikes = 0  # three webdriver exception's and we'll shut down
        while True:

            # get the open/closed status of the shopping cart classes
            try:
                cart = self.check_shopping_cart()
                self.print_cart(cart)

            # handle exceptions
            except ElementDoesNotExist as e:
                strikes += 1
                if strikes >= 3:
                    self.handle_exception(e)
            except Exception as e:
                self.handle_exception(e)
            else:
                strikes = 0

            # wait until the next run
            self.wait(5 * 60)

    def handle_exception(self, e):
        print(e)
        (address, password) = self.logins['gmail']
        send_email(address, password, str(e))

    @staticmethod
    def print_cart(cart):
        print('----')
        printBuffer = ['{0}: {1}'.format(cartClass[0], cartClass[1])
                       for cartClass in cart]
        print('\n'.join(printBuffer))
        print('----')

    def notify_of_status(self, cart, gmailAddr, gmailPassword):
        for course in cart:
                if course[1] != 'Closed':
                    self.send_email(gmailAddr, gmailPassword,
                                    '{0}: {1}'.format(course[0], course[1]))

    def check_shopping_cart(self):
        # create a driver for Wells Fargo
        with MyRedBrowser() as browser:

            # go to wellsfargo.com and login
            browser.nav_home()
            browser.login(*self.logins['myred'])

            browser.nav_to_enrollment_planner()

            with browser.get_panel_browser() as panelBrowser:
                panelBrowser.nav_to_shopping_cart()
                panelBrowser.choose_semester(1)

                cart = panelBrowser.parse_shopping_cart()

                return cart


if __name__ == "__main__":
    EnrollmentChecker().run()
