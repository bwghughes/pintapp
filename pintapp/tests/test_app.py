#!/usr/bin/env python
import os
import sys
sys.path.insert(0, os.pardir)

import json
from flask.ext.testing import TestCase
from pintapp.app import app
from pintapp.models.user import User


class TestRegisterAPI(TestCase):

    def create_app(self):
        return app

    def test_we_can_register_a_new_user(self):
        response = self.client.post("/register",
                                    data=json.dumps(dict(number="447720149993", name="Ben Hughes")),
                                    content_type="application/json")
        new_user = User(**response.json)
        self.assertTrue(new_user.validate())
