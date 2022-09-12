# -*- coding: utf-8 -*-

from test_group import Group
from test_contact import Contact
from test_application import Application
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



    def test_contact_add(self):
        app.login(username="admin", password="secret")
        app.create_new_contact(Contact(name_contact="Maks", mail_contact="feniks3004@mail.ru"))
        app.logout()

