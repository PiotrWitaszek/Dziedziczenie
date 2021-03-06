from typing_extensions import Self
from faker import Faker
fake = Faker("en_US")

class BaseContact:
    def __init__(self, name, surname, email_address,tel):
        self.name = name
        self.surname = surname
        self.email_address = email_address
        self.tel = tel

        self._label_lenght = len(f"{self.name} {self.surname}")
        
    def contact(self):
        return f'I am dialing number {self.tel} and calling {self.name} {self.surname}'  
    
    @property
    def label_lenght(self):
        return self._label_lenght

def create_contacts(kind, quantity):
        while True:
            choice = input("Enter choice (p/b/x):")

            if choice in ('p', 'b',):
                quantity = float(input("Enter number of cards:"))
       
            if choice == 'p':
                contacts.append(human_1)
            elif choice == 'b':
                business_contacts.append(human_1)
            elif choice == 'x':
                exit()
            else:
                print("Invalid input")

if __name__ == "__main__":
    class BusinessContact(BaseContact):
        def __init__(self, business_tel, company, position, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.business_tel = business_tel
            self.company = company
            self.position = position

        def contact(self):
            return f'I am dialing number {self.business_tel} and calling {self.name} {self.surname}'
      
    human_1 = BusinessContact(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(),
              email_address=fake.email(), tel=fake.phone_number(), business_tel=fake.phone_number())

    def create_contacts(kinds, quantity):
        return create_contacts
    
    contacts = []
    business_contacts = []
    print("Select the type of business card:")
    print("p - private")
    print("b - business")
    print("x - exit programm")
    
    
    print(human_1.contact())
    print(human_1.label_lenght)
