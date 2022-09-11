class Contact:
    #from contact import Contact
    def __init__(self, name_contact, mail_contact):
        self.name_contact = name_contact
        self.mail_contact = mail_contact

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