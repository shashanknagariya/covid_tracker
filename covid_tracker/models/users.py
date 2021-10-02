from covid_tracker.models.zones import Zones,zone_color
import uuid
class Users(object):

    user_data = {}

    def __init__(self,name,phone_number,pincode):
        self.id = uuid.uuid1()
        self.name = name
        self.phone_number = phone_number
        self.pincode = pincode
        self.symptom = []
        self.travel_history=None
        self.contact_with_covid_patient = None 
        self.risk_percentage = None
        self.result = 'Negative'
        print(f'UserId : {self.id}')

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
    
    def get_symptom(self):
        return self.symptom
    
    def set_symptom(self,symptom):
        self.symptom = symptom
    
    def get_travel_history(self):
        return self.travel_history
    
    def set_travel_history(self,history):
        self.travel_history = history
    
    def get_contact_with_covid(self):
        return self.contact_with_covid_patient
    
    def set_contact_with_covid(self,contact_with_covid):
        self.contact_with_covid_patient = contact_with_covid
    
    def get_risk_percentage(self):
        if not self.get_symptom() and not self.get_travel_history() and not self.get_contact_with_covid():
            return "risk percentage 5%"
        elif len(self.get_symptom()) == 1 and self.get_travel_history() and self.get_contact_with_covid():
            return "risk percentage 50%"
        elif len(self.get_symptom()) == 2 and self.get_travel_history() and self.get_contact_with_covid():   
            return "risk percentage 75%"
        elif len(self.get_symptom()) > 2 and self.get_travel_history() and self.get_contact_with_covid(): 
            return "risk percentage 95%"
        else:
            return "No risk"

    def get_result(self):
        return self.result
    
    def set_result(self,result):
        self.result = result
        return True
    