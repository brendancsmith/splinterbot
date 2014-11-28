from browsers import WFBrowser


def main():
    with WFBrowser() as browser:
        browser.visit('http://wellsfargo.com')

        #browser.login('foo', 'bar')


if __name__ == "__main__":
    main()
