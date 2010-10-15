import unittest


class TestPatches(unittest.TestCase):

    def test_patches_applied(self):
        pass


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestPatches))
    return suite
