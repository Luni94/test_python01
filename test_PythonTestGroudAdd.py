# -*- coding: utf-8 -*-

from test_group import Group
from test_contact import Contact
from test_application import Application
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture




    
def test_group_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="addressss"))
    app.logout()

def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name=""))
    app.logout()



def test_contact_add(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(name_contact="Maks", mail_contact="feniks3004@mail.ru"))
    app.logout()

def test_empty_add(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(name_contact="", mail_contact=''))
    app.logout()