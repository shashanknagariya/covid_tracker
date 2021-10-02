import uuid 

class Admin(object):
    def __init__(self,name,phone,pincode):
        self.id = uuid.uuid1()
        self.name = name
        self.phone_number = phone
        self.pincode = pincode
        self.symptom = None
        self.travel_history=None
        self.contact_with_covid_patient = None 
        print(f'AdminId: {self.id}')

    def get_name(self):
        return self.get_name
    
    def set_name(self,name):
        self.name = name 
    
    def get_phone_numer(self):
        return self.phone_number
    
    def set_phone_numer(self,phone):
        self.phone_number = phone 
    
    def get_pincode(self):
        return self.pincode
    
    def set_pincode(self,pin):
        self.pincode = pin 