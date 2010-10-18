from .base import ATRefSpeedupTestCase


class TestEngine(ATRefSpeedupTestCase):

    def test_spam(self):
        pass


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestEngine))
    return suite
