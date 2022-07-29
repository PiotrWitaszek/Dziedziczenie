from faker import Faker
fake = Faker("en_US")

class BaseContact:
    def __init__(self, name, surname, email_address, tel):
        self.name = name
        self.surname = surname
        self.email_address = email_address
        self.tel = tel

        self._label_lenght = len(f"{self.name} {self.surname}")
        
    def contact(self):
        return f'I am dialing number {self.tel} and calling {self.name} {self.surname}'  

    def __str__(self):
        return f'{self.name} {self.surname} {self.email_address} {self.tel}{self.business_tel} {self.company} {self.position}'

    def __repr__(self):
        return f'{self.name} {self.surname} {self.email_address} {self.tel}'
    
    @property
    def label_lenght(self):
        return self._label_lenght

class BusinessContact(BaseContact):
        def __init__(self, business_tel, company, position, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.business_tel = business_tel
            self.company = company
            self.position = position

        def contact(self):
            return f'I am dialing number {self.business_tel} and calling {self.name} {self.surname}'

def create_contacts():
    print("Select the type of business card:")
    print("p - private")
    print("b - business")
    print("x - exit programm")
    while True:
            choice = input("Enter choice (p/b/x):")

            if choice in ('p', 'b',):
                quantity = int(input("Enter number of cards:"))
       
            if choice == 'p':
                contacts = []
                for i in range(quantity):
                    contacts.append(BaseContact(name=fake.first_name(), surname=fake.last_name(), email_address=fake.email(), tel=fake.phone_number()))
                print(contacts)
            elif choice == 'b':
                business_contacts = []
                for i in range(quantity):
                    business_contacts.append([fake.first_name(), fake.last_name(), fake.email(), fake.phone_number(), fake.company(), fake.job() , fake.phone_number()])
                print(business_contacts)
            elif choice == 'x':
                exit()
            else:
                print("Invalid input")

if __name__ == "__main__":  
    create_contacts()