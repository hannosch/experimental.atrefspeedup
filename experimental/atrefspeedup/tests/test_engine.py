from Products.CMFCore.utils import getToolByName

from .base import ATRefSpeedupTestCase


class TestGetReferences(ATRefSpeedupTestCase):

    def afterSetUp(self):
        self.rc = getToolByName(self.portal, 'reference_catalog')

    def test_none(self):
        doc1 = self.portal.doc1
        self.assertEquals(self.rc.getReferences(doc1), [])
        self.assertEquals(self.rc.getReferences(doc1, 'relatesTo'), [])

    def test_single(self):
        doc1 = self.portal.doc1
        doc2 = self.portal.doc2
        doc1.setRelatedItems([doc2.UID()])
        result = self.rc.getReferences(doc1)
        self.assertEquals(result[0].getTargetObject(), doc2)
        result = self.rc.getReferences(doc1, 'relatesTo')
        self.assertEquals(result[0].getTargetObject(), doc2)


class TestGetBackReferences(ATRefSpeedupTestCase):

    def afterSetUp(self):
        self.rc = getToolByName(self.portal, 'reference_catalog')

    def test_none(self):
        doc1 = self.portal.doc1
        self.assertEquals(self.rc.getBackReferences(doc1), [])
        self.assertEquals(self.rc.getBackReferences(doc1, 'relatesTo'), [])

    def test_single(self):
        doc1 = self.portal.doc1
        doc2 = self.portal.doc2
        doc1.setRelatedItems([doc2.UID()])
        result = self.rc.getBackReferences(doc2)
        self.assertEquals(result[0].getSourceObject(), doc1)
        result = self.rc.getBackReferences(doc2, 'relatesTo')
        self.assertEquals(result[0].getSourceObject(), doc1)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestGetReferences))
    suite.addTest(makeSuite(TestGetBackReferences))
    return suite
