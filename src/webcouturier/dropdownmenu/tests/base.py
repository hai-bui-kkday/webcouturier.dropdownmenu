# -*- coding: utf-8 -*-
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from webcouturier.dropdownmenu.tests import layer

import unittest2 as unittest


class Helper(unittest.TestCase):

    @property
    def portal(self):
        return self.layer['portal']

    def setRoles(self, roles):
        setRoles(self.portal, TEST_USER_ID, roles)


class DropdownmenuTestCase(Helper):

    layer = layer.DROPDOWNMENU_INTEGRATION
