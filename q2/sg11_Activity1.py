class Patient:#Parent class
    def __init__(self, name: str, bill_amount: float):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount: float):
        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative.")

    def calculate_bill(self):#used to calculated the bill amount
        return self.bill_amount

    def display_patient_type(self):#displays the patient type
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):#Subclass of Patient
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)#allows subclass to call methods

    def calculate_bill(self):#calculate bill with 20% discount
        discount = 0.2  # 20% discount for senior patients
        return self.bill_amount * (1 - discount)

    def display_patient_type(self):#displays the patient type
        print("Patient Type: Senior Citizen")

class PhilHealthPatient(Patient):#Subclass of Patient
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)#allows subclass to call methods

    def calculate_bill(self):#calculate bill with 15% discount
        discount = 0.15  # 15% discount for PhilHealth patients
        return self.bill_amount * (1 - discount)

    def display_patient_type(self):#displays the patient type
        print("Patient Type: PhilHealth Member")

p1 = Patient("Juan Dela Cruz", 15000.00)#object of Patient
p2 = SeniorPatient("Maria Santos", 15000.00)#object of SeniorPatient
p3 = PhilHealthPatient("Pedro Reyes", 15000.00)#object of PhilHealthPatient

#Execution
print("Hospital Billing System")
print("-----------------------")
print(f'Patient Name: {p1.get_name()}')
p1.display_patient_type()
print(f'Original Bill: ₱{p1.get_bill_amount():,.2f}')
print(f'Final Bill: ₱{p1.calculate_bill():,.2f}')
print()

print(f'Patient Name: {p2.get_name()}')
p2.display_patient_type()
print(f'Original Bill: ₱{p2.get_bill_amount():,.2f}')
print(f'Final Bill: ₱{p2.calculate_bill():,.2f}')
print()

print(f'Patient Name: {p3.get_name()}')
p3.display_patient_type()
print(f'Original Bill: ₱{p3.get_bill_amount():,.2f}')
print(f'Final Bill: ₱{p3.calculate_bill():,.2f}')
