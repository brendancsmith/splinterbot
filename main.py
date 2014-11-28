from splinter import Browser


def main():
    browser = Browser()
    browser.visit('http://wellsfargo.com')

    browser.quit()

if __name__ == "__main__":
    main()
