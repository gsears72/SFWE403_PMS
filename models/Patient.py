from datetime import datetime

def canonical_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        try:
            date = datetime.strptime(date_str, '%m/%d/%Y')
        except ValueError:
            try:
                date = datetime.strptime(date_str, '%d-%b-%Y')
            except ValueError:
                return None
    return date.strftime('%Y-%m-%d')



class Patient:
    def __init__(self, name, birth_date, address, phone_number, email, insurance):
        self.name = name
        self.birth_date = canonical_date(birth_date)
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.insurance = insurance

    def __str__(self):
        return "Patient Name: {}\nBirth Date: {}\nAddress: {}\nPhone Number: {}\nEmail: {}\nInsurance: {}".format(self.name, self.birth_date, self.address, self.phone_number, self.email, self.insurance)
    
    def __repr__(self):
        return "Patient('{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.birth_date, self.address, self.phone_number, self.email, self.insurance)
    
    def __eq__(self, other):
        return self.name == other.name and self.birth_date == other.birth_date and self.address == other.address and self.phone_number == other.phone_number and self.email == other.email and self.insurance == other.insurance
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.name, self.birth_date, self.address, self.phone_number, self.email, self.insurance))
    
    def get_name(self):
        return self.name
    
    def get_birth_date(self):
        return self.birth_date
    
    def get_address(self):
        return self.address
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_email(self):
        return self.email
    
    def get_insurance(self):
        return self.insurance
    
    def set_name(self, name):
        self.name = name

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_email(self, email):
        self.email = email

    def set_insurance(self, insurance):
        self.insurance = insurance

    
    