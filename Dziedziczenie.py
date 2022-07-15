class BaseContact:
    def __init__(self, name, surname, tel, mail):
        self.name = name
        self.surname = surname
        self.tel = tel
        self.mail = mail

    def contact(self):
        return f'I am dialing number {self.tel} and calling {self.name} {self.surname}'  

    @property
    def label_lenght(self):
        return sum([len(self.name), len(self.surname),+1])
  

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
        return sum([len(self.name), len(self.surname),+1])


def create_contacts(kind, quantity):

    contacts = []
    for i in range(quantity):
        if kind == 'b':
            business_contacts.append(BusinessContact)
        elif kind == 'p':
            contacts.append(BaseContact)
    return contacts

contacts = []
business_contacts = []

if __name__ == "__main__":
    print("Select the type of business card:")
    print("p - private")
    print("b - business")
    print("x - exit programm")
    while True:
        choice = input("Enter choice (p/b/x):")

        if choice in ('p', 'b',):
            quantity = float(input("Enter number of cards:"))
       
        if choice == 'p':
            for i in range(quantity):
                contacts.append(BaseContact)
    #Czy da się tutaj for in range zastosować i czy jednak robić to tylko w funkcji create_contacts?
        elif choice == 'b':
            for i in range(quantity):
                business_contacts.append(BusinessContact)
        elif choice == 'x':
            exit()
        else:
            print("Invalid input")

        

