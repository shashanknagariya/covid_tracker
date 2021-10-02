from covid_tracker.models.users import Users

class user_manage(object):
    def register_user(name,phone_numer,pincode):
        user_obj =  Users(name,phone_numer,pincode)
        user_obj.user_data[user_obj.id] = user_obj
        return user_obj
    
    def self_assessment(user_obj,symptoms,travel_history,contact_covid):
        user_obj.set_symptom(symptoms)
        user_obj.set_travel_history(travel_history)
        user_obj.set_contact_with_covid(contact_covid)
        return user_obj.get_risk_percentage()
    

