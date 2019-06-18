# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import imio.demo.restapi


class ImioDemoRestapiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=imio.demo.restapi)


IMIO_DEMO_RESTAPI_FIXTURE = ImioDemoRestapiLayer()


IMIO_DEMO_RESTAPI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMIO_DEMO_RESTAPI_FIXTURE,), name="ImioDemoRestapiLayer:IntegrationTesting"
)


IMIO_DEMO_RESTAPI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IMIO_DEMO_RESTAPI_FIXTURE,), name="ImioDemoRestapiLayer:FunctionalTesting"
)


IMIO_DEMO_RESTAPI_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(IMIO_DEMO_RESTAPI_FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="ImioDemoRestapiLayer:AcceptanceTesting",
)
