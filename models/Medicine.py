
class Medicine:
    def __init__(self, name, brand, price, dosage, consumptionForm, medicineInfo): 
        self.name = name
        self.brand = brand
        self.price = price
        self.dosage = dosage
        self.consumptionForm = consumptionForm
        self.medicineInfo = medicineInfo

    def __str__(self):
        return self.name + " " + self.brand + " " + self.price + " " + self.dosage + " " + self.consumptionForm + " " + self.medicineInfo
    
    def __hash__(self):
        return hash((self.name, self.brand, self.price, self.dosage, self.consumptionForm, self.medicineInfo))
    
    def get_name(self):
        return self.name
    
    def get_brand(self):
        return self.brand
    
    def get_price(self):
        return self.price
    
    def get_dosage(self):
        return self.dosage
    
    def get_consumptionForm(self):
        return self.consumptionForm
    
    def get_medicineInfo(self):
        return self.medicineInfo
    
    def set_name(self, name):
        self.name = name

    def set_brand(self, brand):
        self.brand = brand

    def set_price(self, price):
        self.price = price

    def set_dosage(self, dosage):
        self.dosage = dosage

    def set_consumptionForm(self, consumptionForm):
        self.consumptionForm = consumptionForm

    def set_medicineInfo(self, medicineInfo):
        self.medicineInfo = medicineInfo

    
