from covid_tracker.models.admins import Admin
from covid_tracker.models.users import Users

class admin_manage(object):
    admin_user_details = dict()

    def register_admin(name,phone_number,pincode):
        return Admin(name,phone_number,pincode)

    def update_covid_result(user_id,admin,result):
        user_obj = Users.user_data.get(user_id,None)  
        if user_obj:
            admin_manage.admin_user_details[admin] = user_obj
            print('updated :',user_obj.set_result(result))
        else:
            print('user does not exists')
    

