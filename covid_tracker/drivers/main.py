import sys
sys.path.insert(0,r'C:\Users\Lenovo\Documents\Udaan\udaan')
#importing models
from covid_tracker.models.admins import Admin
from covid_tracker.models.users import Users
from covid_tracker.models.zones import Zones

#importing managers

from covid_tracker.managers.admin_manager import admin_manage
from covid_tracker.managers.user_manager import user_manage

#Register user 

user1 = user_manage.register_user('shashank','123456789','471001')
print(user_manage.self_assessment(user1,['cough','cold'],True,True))

#Register Admin

Admin1 = admin_manage.register_admin('admin1','1245','471105')
print(admin_manage.update_covid_result(user1.id,Admin1,'Positive'))
