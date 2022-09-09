# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from contact import Contact
import unittest

class PythonTestGroudAdd(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_group_add(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="addressss"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name=""))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_contact_add(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(name_contact="Maks", mail_contact="feniks3004@mail.ru"))
        self.save_contact_info(wd)
        self.open_contacts_page(wd)
        self.logout(wd)

    def open_contacts_page(self, wd):
        # open contacts page
        wd.find_element_by_link_text("home").click()

    def save_contact_info(self, wd):
        # save new  contact info
        wd.find_element_by_xpath("//input[21]").click()

    def create_new_contact(self, wd, contact):
        # create new contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name_contact)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.mail_contact)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_name("new").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
