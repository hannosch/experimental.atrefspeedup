from Products.CMFCore.utils import getToolByName

from .base import ATRefSpeedupTestCase


class TestGetReferences(ATRefSpeedupTestCase):

    def afterSetUp(self):
        self.rc = getToolByName(self.portal, 'reference_catalog')

    def test_none(self):
        doc1 = self.portal.doc1
        self.assertEquals(self.rc.getReferences(doc1), [])
        self.assertEquals(self.rc.getReferences(doc1, 'relatesTo'), [])


class TestGetBackReferences(ATRefSpeedupTestCase):

    def afterSetUp(self):
        self.rc = getToolByName(self.portal, 'reference_catalog')

    def test_none(self):
        # getBackReferences(self, object, relationship=None, targetObject=None):
        doc1 = self.portal.doc1
        self.assertEquals(self.rc.getBackReferences(doc1), [])
        self.assertEquals(self.rc.getBackReferences(doc1, 'relatesTo'), [])


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestGetReferences))
    suite.addTest(makeSuite(TestGetBackReferences))
    return suite
