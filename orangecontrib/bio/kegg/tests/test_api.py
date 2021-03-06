import unittest
import doctest

from orangecontrib.bio import kegg


class TestApi(unittest.TestCase):
    pass


def load_tests(loader, tests, ignore):
    tests.addTests(
        doctest.DocTestSuite(kegg, optionflags=doctest.ELLIPSIS))
    return tests
