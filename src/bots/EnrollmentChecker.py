#------------------------------ imports --------------------------------

# standard modules
from getpass import getpass

# intra-project modules
from browsers import MyREDBrowser
import utils
from gmail import Gmail

# external libraries
# N/A

#-----------------------------------------------------------------------


def main():
    """Checks MyRED to see if classes in the shopping cart for next
    semester are open or closed."""

    # get login details from terminal
    myredUsername, myredPassword = ask_login_details('MyRED Login',
                                                     'NUID')
    gmailAddr, gmailPassword = ask_login_details('Gmail Login',
                                                 'Email address')


    while True:
        cart = check_shopping_cart(myredUsername, myredPassword)

        print_cart(cart)
        utils.wait(60 * 5)


def ask_login_details(loginTitle='Login:',
                      usernameLabel='Username', passwordLabel='Password'):
    print(loginTitle)
    print('=' * len(loginTitle))
    username = raw_input(usernameLabel + ': ')
    password = getpass(passwordLabel + ': ')

    return username, password


def print_cart(cart):
    print('----')
    printBuffer = ['{0}: {1}'.format(cartClass[0], cartClass[1])
                   for cartClass in cart]
    print('\n'.join(printBuffer))
    print('----')


def notify_of_status(cart, gmailAddr, gmailPassword):
    for course in cart:
            if course[1] != 'Closed':
                send_email(gmailAddr, gmailPassword,
                           '{0}: {1}'.format(course[0], course[1]))


def check_shopping_cart(username, password):
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


def send_email(gmailAddr, gmailPassword, msg):
    with Gmail(gmailAddr, gmailPassword) as server:
        server.sendmail(gmailAddr, [gmailAddr], msg)

if __name__ == "__main__":
    main()
