from browsers import WFBrowser


def main():
    browser = WFBrowser()
    browser.visit('http://wellsfargo.com')

    #browser.login('foo', 'bar')

    browser.quit()


if __name__ == "__main__":
    main()
