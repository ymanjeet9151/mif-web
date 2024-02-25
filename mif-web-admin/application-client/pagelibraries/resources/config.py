import os
import sys


class Config(object):
    """Configuration variables for this test suite
    This creates a variable named CONFIG (${CONFIG} when included
    in a test as a variable file.
    Example:
    *** Settings ***
    | Variable | ../resources/config.py
    *** Test Cases ***
    | Example
    | | log | username: ${CONFIG}.username
    | | log | root url: ${CONFIG}.root_url
    """
    def __init__(self):
        _here = os.path.dirname(__file__)
        self.data_file_path = \
            _here[:_here.index("pagelibraries")] + "testdata//datafiles//"
        sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..")))
        sys.path.insert(0, os.path.abspath(os.path.join(_here)))
        self.root_url = 'about:blank'
        self.url = 'https://dev-mifadmin.makeitfree.com/'
        self.stage_url = 'https://stage-mifadmin.makeitfree.com/'
        self.host = 'dev-mifadmin.makeitfree'
        self.domain = 'stage'
        self.endpoint = 'auth/signin'

    def __str__(self):
        """
        Used for string representation of an object
        """
        return "<Config: %s>" % str(self.__dict__)


# This creates a variable that robot can see
CONFIG = Config()
