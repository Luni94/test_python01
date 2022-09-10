# -*- coding: utf-8 -*-

from group import Group
from application import Application
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroi())
    return fixture




    
    def test_group_add(self):
        app.login( username="admin", password="secret")
        app.create_group( Group(name="addressss"))
        app.logout()

    def test_empty_group(self):
        app.login( username="admin", password="secret")
        app.create_group( Group(name=""))
        app.logout()


