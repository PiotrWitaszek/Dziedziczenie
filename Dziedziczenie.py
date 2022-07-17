from faker import Faker
fake = Faker("en_US")
class BaseContact:
    def __init__(self, name, surname, tel, mail):
        self.name = name
        self.surname = surname
        self.tel = tel
        self.mail = mail

        self.label_lenght = len(f"{self.name} {self.surname}")

    def contact(self):
        return f'I am dialing number {self.tel} and calling {self.name} {self.surname}'  

    @property
    def label_lenght(self):
        return self.label_lenght
  
class BusinessContact(BaseContact):
    def __init__(self, position, company, business_tel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_tel = business_tel
        
    def contact(self):
        return f'I am dialing number {self.business_tel} and calling {self.name} {self.surname}'    

    @property
    def label_lenght(self):
        return self.label_lenght

if __name__ == "__main__":
    contacts = []
    business_contacts = []
    print("Select the type of business card:")
    print("p - private")
    print("b - business")
    print("x - exit programm")
    while True:
        choice = input("Enter choice (p/b/x):")

        if choice in ('p', 'b',):
            quantity = float(input("Enter number of cards:"))
       
        if choice == 'p':
            contacts.append(BaseContact)
        elif choice == 'b':
            business_contacts.append(BusinessContact)
        elif choice == 'x':
            exit()
        else:
            print("Invalid input")
    
    def create_contacts(kind, quantity):
        for i in range(int(quantity)):
            if kind == 'b':
                human_1 = BusinessContact(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(),
              mail=fake.email(), tel=fake.phone_number(), business_tel=fake.phone_number())

            elif kind == 'p':
                human_2 = BaseContact(name=fake.first_name(), surname=fake.last_name(), mail=fake.email(), tel=fake.phone_number())
        return contacts
    
    human_1 = BusinessContact(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(),
              mail=fake.email(), tel=fake.phone_number(), business_tel=fake.phone_number())
    print(human_1)
    print(human_1.BaseContact())
    print(human_1.BusinessContact())
    print(human_1.label_lenght)
    print() 