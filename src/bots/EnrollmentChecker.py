#------------------------------ imports --------------------------------

# standard modules
from getpass import getpass

# intra-project modules
from browsers import MyREDBrowser
import utils

# external libraries
# N/A

#-----------------------------------------------------------------------


def main():
    """Checks MyRED to see if classes in the shopping cart for next
    semester are open or closed."""

    # get login details from terminal
    username = raw_input('NUID: ')
    password = getpass('MyRED Password: ')

    while True:
        check_enrollment_availability(username, password)
        utils.wait(60 * 5)


def check_enrollment_availability(username, password):
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

            printBuffer = ['{0}: {1}'.format(cartClass[0], cartClass[1])
                           for cartClass in cart]
            print('\n'.join(printBuffer))


if __name__ == "__main__":
    main()
