"""Browsy - A Qt Web Browser written in Python.
"""
import getopt
import sys

from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication, QGridLayout, QLineEdit, QWidget
from PyQt4.QtWebKit import QWebView


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


class UrlInput(QLineEdit):
    def __init__(self, browser):
        super(UrlInput, self).__init__()
        self.browser = browser
        # add event listener on "enter" pressed
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        url = QUrl(self.text())
        # load url into browser frame
        self.browser.load(cleanUrl(url))
        self.browser.show()


def cleanUrl(url):
    # TODO: make sure url is actually navigable (e.g., has http://)
    return QUrl(url)


def main(argv=None):
    if argv is None:
        # you don't want to use a sys.argv as a defaul argument as it would be
        # set when the function is defined, *not* when it's called
        argv = sys.argv

    try:
        # parse command line options
        try:
            # process options and argument
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

    app = QApplication(sys.argv)

    # create grid layout
    grid = QGridLayout()

    browser = QWebView()
    if len(argv) > 1:
        browser.load(cleanUrl(argv[1]))
    # browser frame at row 2 column 0 of our grid
    grid.addWidget(browser, 2, 0)

    url_input = UrlInput(browser)
    # url_input at row 1 column 0 of our grid
    grid.addWidget(url_input, 1, 0)

    # main app window
    main_frame = QWidget()
    main_frame.setLayout(grid)
    main_frame.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
