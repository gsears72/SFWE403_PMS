from models.Staff import PharmacyManager

class PharmacyManagerController:
    def __init__(self, name):
        self._pharmacy_manager = PharmacyManager(name)
        



    def run(self):
        while 1:
            mangerAction = input("Inventory, Reports, User Management, Log Out\n")
            if (mangerAction == "Inventory"):
                update = input("would you like to: update quantity, delete\n")
                if (update == "update quantity"):
                    self._pharmacy_manager.updateInventory()
                elif (update == "delete"):
                    self._pharmacy_manager.deleteInventory()
                else:
                    print("invalid input")
            elif (mangerAction == "Reports"):
                print("Reports")
            elif (mangerAction == "User Management"):    
                print("What you like to do (Create Pharmacy Account, Remove Patient, Create Patient, Update Patient Information)")    
                response = str(input()).strip().lower()
                if response == "create pharmacy account":    
                    print("Create User Account? (Y/N)")
                    action = str(input()).strip().lower()
                    if action == 'y':
                        self._pharmacy_manager.createPharmacyAccount()
                    else:
                        continue

                elif response == "remove patient":
                    print("Remove Patient? (Y/N)")
                    action = str(input()).strip().lower()
                    if action == 'y':
                        self._pharmacy_manager.removePatient()
                    else:
                        continue

                elif response == "create patient":
                    print("Create Patient? (Y/N)")
                    action = str(input()).strip().lower()
                    if action == 'y':
                        self._pharmacy_manager.createPatient()
                    else:
                        continue

                elif response == "update patient information":
                    print("Update Patient Information? (Y/N)")
                    action = str(input()).strip().lower()
                    if action == 'y':
                        self._pharmacy_manager.UpdateCustomer()
                    else:
                        continue
                    
            elif (mangerAction == "Log Out"):
                break
            else:
                print("error")