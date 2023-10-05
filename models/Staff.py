from datetime import datetime
from abc import ABC, abstractmethod

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

class Staff(ABC):
    @abstractmethod
    def __init__(self, name, birth_date, address, phone_number, email, username, password):
        self.name = name
        self.birth_date = canonical_date(birth_date)
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    @abstractmethod
    def __str__(self):
        return "Staff Name: {}\nBirth Date: {}\nAddress: {}\nPhone Number: {}\nEmail: {}\nUsername: {}\nPassword: {}".format(self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password)

    @abstractmethod
    def __repr__(self):
        return "Staff('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password)
    
    @abstractmethod
    def __eq__(self, other):
        return self.name == other.name and self.birth_date == other.birth_date and self.address == other.address and self.phone_number == other.phone_number and self.email == other.email and self.username == other.username and self.password == other.password
    
    @abstractmethod
    def __ne__(self, other):
        return not self.__eq__(other)
    
    @abstractmethod
    def __hash__(self):
        return hash((self.name, self.birth_date, self.address, self.phone_number, self.email, self.username, self.password))
    

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
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
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

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def createPatient():

    def modifyPatient():

    def enterPrescription():

    

class PharmacyManager(Staff):
    def __init__(self, name, birth_date, address, phone_number, email, username, password, pharmacy):
    
    def __str__(self):

    
    def __repr__(self):

    
    def __eq__(self, other):

    
    def __ne__(self, other):

    
    def __hash__(self):

    def createPharmacyAccount():

    def removePatient():

    def recoverStaffAccount():

    def orderMedication():

    def updateInventory():

    def removeItem():

    def generateFinancialReport():

    def generateInventoryReport():

    
    

class Pharmacist(Staff):
    def __init__(self, name, birth_date, address, phone_number, email, username, password, pharmacy):

    
    def __str__(self):

    
    def __repr__(self):

    
    def __eq__(self, other):

    
    def __ne__(self, other):

    
    def __hash__(self):

    def removePatient():
        
    def checkAvailability():

    def fillPrescription():
    
    
        

class PharmacistTechnician(Staff):
    def __init__(self, name, birth_date, address, phone_number, email, username, password, pharmacy):
        
    
    def __str__(self):
        
    
    def __repr__(self):
        
    
    def __eq__(self, other):
        
    
    def __ne__(self, other):
        
    
    def __hash__(self):
        
    
    

class Cashier(Staff):
    def __init__(self, name, birth_date, address, phone_number, email, username, password):

    
    def __str__(self):

    
    def __repr__(self):

    
    def __eq__(self, other):

    
    def __ne__(self, other):

    
    def __hash__(self):
        
    
    
    
    

    


    