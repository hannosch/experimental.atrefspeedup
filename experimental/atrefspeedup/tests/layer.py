from collective.testcaselayer.ptc import BasePTCLayer, ptc_layer
from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc


class ATRefSpeedupLayer(BasePTCLayer):
    """ layer for integration tests """

    def afterSetUp(self):
        import experimental.atrefspeedup
        fiveconfigure.debug_mode = True
        zcml.load_config("configure.zcml", experimental.atrefspeedup)
        fiveconfigure.debug_mode = False
        ztc.installPackage("experimental.atrefspeedup", quiet=True)

    def beforeTearDown(self):
        pass


atrefspeedup = ATRefSpeedupLayer(bases=[ptc_layer])
