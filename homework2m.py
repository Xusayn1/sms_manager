class Contact:
    def __init__(self,name,email,phone_number, age):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.age = age
        self.base = []
        self.base2 = []

    def add_contact(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone_number = input("Enter your phone number: ")
        age = int(input("Enter your age: "))
        contact = Contact(name,email,phone_number,age)
        self.base.append(contact)

    def view_contact(self):
        for contact in self.base:
            print(f' name:{contact.name} email:{contact.email} phone_number:{contact.phone_number} age:{contact.age}')


    def delete_contact(self):
        name = input("Enter the name: ")
        for contact in self.base:
            if contact.name == name:
                self.base.remove(contact)
                print('deleted successfully')

    def manager_contact(self):
        print("***** Manager Contact *****")
        while True:
            print('1. add contact \n 2. view contact \n 3. delete contact \n 4. Exit')
            code = input("Enter your code: ")
            if code == '1':
                self.add_contact()
            elif code == '2':
                self.view_contact()
            elif code == '3':
                self.delete_contact()
            else:
                print('Exiting...')
                break

    def send_message(self):
        name = input("Enter the name: ")
        sms = input("Enter your message: ")

        for contact in self.base:
            if contact.name == name:
                self.base2.append((name, sms))
                print("Message sent successfully")
                return

        print("User not found")

    def view_message(self):
        for name, sms in self.base2:
            print(f'name:{name} sms:{sms}')

    def delete_message(self):
        name = input("Enter the name: ")
        before = len(self.base2)
        self.base2 = [msg for msg in self.base2 if msg[0] != name]
        after = len(self.base2)
        if before == after:
            print("Message not found")
        else:
            print("Message deleted successfully")

    def sms_manager(self):
        print('**** SMS Manager ****')
        while True:
            print('1. send message \n2. view message \n3. delete message \n4. Exit')
            code = input('Enter your code: ')
            if code == '1':
                self.send_message()
            elif code == '2':
                self.view_message()
            elif code == '3':
                self.delete_message()
            else:
                print("Exiting...")
                break

    def contact_sms_manager(self):
        print('**** Contact SMS Manager ****')
        while True:
            print('1. contact manager \n 2. sms manager \n 3. Exit')
            code = input('Enter your code: ')
            if code == '1':
                self.manager_contact()
            elif code == '2':
                self.sms_manager()
            else:
                print("Exiting...")
                break

if __name__ == '__main__':
    user = Contact('Xusayn','xusayn@iclodu.com','998901234567','22')
    user.contact_sms_manager()








