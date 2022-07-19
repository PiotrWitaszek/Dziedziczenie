from faker import Faker
fake = Faker("en_US")

class BaseContact:
    def __init__(self, name, surname, email_address,tel):
        self.name = name
        self.surname = surname
        self.email_address = email_address
        self.tel = tel
    
    def contact(self):
        return f'I am dialing number {self.tel} and calling {self.name} {self.surname}'  
    
    def businesscontact(self):
        return f'I am dialing number {self.business_tel} and calling {self.name} {self.surname}'  
    
    @property
    def label_lenght(self):
        return len(f"{self.name} {self.surname}")


class BusinessContact(BaseContact):
    def __init__(self, business_tel, company, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_tel = business_tel
        self.company = company
        self.position = position
human_1 = BusinessContact(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(),
              email_address=fake.email(), tel=fake.phone_number(), business_tel=fake.phone_number())
print(human_1)
print(human_1.contact())
print(human_1.businesscontact())
print(human_1.label_lenght)
