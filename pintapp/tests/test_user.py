from pintapp.models.user import User

class TestUser(object):
    def setup(self):
        self.u = User(name="Ben", mobile_number="447720149993")

    def teardown(self):
        pass

    def test_user_is_valid(self):
        assert self.u.validate()




