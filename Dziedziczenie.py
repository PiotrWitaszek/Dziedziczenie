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
                quantity = float(input("Enter number of cards:"))
       
            if choice == 'p':
                contacts = []
                for human_1 in range(int(quantity)):
                    contacts.append(human_1)
                print(contacts)
            elif choice == 'b':
                business_contacts = []
                for human_1 in range(int(quantity)):
                    business_contacts.append(human_1)
                print(business_contacts)
            elif choice == 'x':
                exit()
            else:
                print("Invalid input")

if __name__ == "__main__":  
    human_1 = BusinessContact(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(),
              email_address=fake.email(), tel=fake.phone_number(), business_tel=fake.phone_number())
    create_contacts()
    
   