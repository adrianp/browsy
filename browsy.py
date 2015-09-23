"""Browsy - A Qt Web Browser written in Python.
"""
import getopt
import sys

from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def process(arg):
    # TODO: implement
    print("arg:", arg)


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
        for arg in args:
            process(arg)
        # TODO: implement option handling
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

    app = QApplication(argv)

    browser = QWebView()
    browser.load(QUrl(argv[1]))
    browser.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
