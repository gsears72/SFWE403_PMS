class Prescription:
    def __init__(self, prescription, customerID, startDate, endDate, medication, quantity, strength, refills, instructions, prescriber):
        self.prescription = prescription
        self.customerID = customerID
        self.startDate = startDate
        self.endDate = endDate
        self.medication = medication
        self.quantity = quantity
        self.strength = strength
        self.refills = refills
        self.instructions = instructions
        self.prescriber = prescriber
