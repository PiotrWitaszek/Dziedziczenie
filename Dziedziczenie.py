

class BaseContact:
    def __init__(self, name, surname, tel, mail):
        self.name = name
        self.surname = surname
        self.tel = tel
        self.mail = mail

    def contact(self):
        return f'I am dialing number {self.tel} and calling {self.name} {self.surname}'    

Anton = BaseContact(name='Antoni', surname='Dur', tel='8535873', mail='gjjg@jgdj.de')
print(Anton)
class BusinessContact(BaseContact):
    def __init__(self, position, company, business_tel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_tel = business_tel
        
    def contact(self):
        return f'I am dialing number {self.business_tel} and calling {self.name} {self.surname}'    

