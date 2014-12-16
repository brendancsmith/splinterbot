#------------------------------ imports --------------------------------

# standard modules
# N/A

# intra-project modules
from gmail import GmailServer

from splinterbot.bot import Bot
from splinterbot.browsers import MyREDBrowser

# external libraries
from splinter.exceptions import ElementDoesNotExist

#-----------------------------------------------------------------------


class EnrollmentChecker(Bot):

    def run(self):
        """Checks MyRED to see if classes in the shopping cart for next
        semester are open or closed."""

        # get login details from terminal
        myredUsername, myredPassword = self.ask_login_details('MyRED Login',
                                                              'NUID')
        gmailAddr, gmailPassword = self.ask_login_details('Gmail Login',
                                                          'Email address')

        # Send a non-error email to verify it's working
        #send_email(gmailAddr, gmailPassword,
        #           'EnrollmentChecker process has started.')

        strikes = 0  # three webdriver exception's and we'll shut down
        while True:

            # get the open/closed status of the shopping cart classes
            try:
                cart = self.check_shopping_cart(myredUsername, myredPassword)
                self.print_cart(cart)

            # handle exceptions
            except ElementDoesNotExist as e:
                strikes += 1
                if strikes >= 3:
                    print(e)
                    self.send_email(gmailAddr, gmailPassword, str(e))
            except Exception as e:
                print(e)
                self.send_email(gmailAddr, gmailPassword, str(e))
            else:
                strikes = 0

            # wait until the next run
            self.wait(5 * 60)

    def print_cart(self, cart):
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

    def check_shopping_cart(self, username, password):
        # create a driver for Wells Fargo
        with MyREDBrowser() as browser:

            # go to wellsfargo.com and login
            browser.nav_home()
            browser.login(username, password)

            browser.nav_to_enrollment_planner()

            with browser.get_panel_browser() as panelBrowser:
                panelBrowser.nav_to_shopping_cart()
                panelBrowser.choose_semester(1)

                cart = panelBrowser.parse_shopping_cart()

                return cart

    def send_email(self, gmailAddr, gmailPassword, msg):
        with GmailServer(gmailAddr, gmailPassword) as mailServer:
            mailServer.sendmail(gmailAddr, [gmailAddr], msg)


if __name__ == "__main__":
    EnrollmentChecker().run()
