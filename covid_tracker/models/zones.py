from collections import defaultdict
from enum import Enum

class zone_color(Enum):
    GREEN = 1
    ORANGE = 2
    RED = 3 

class Zones(object):
    pincode_user_mapping = defaultdict(list)

    def __init__(self,pincode):
        self.pincode = pincode
        self.color = zone_color.GREEN
    
    def get_pincode(self):
        return self.pincode
    
    def set_pincode(self,pincode):
        self.pincode = pincode
    
    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color = color 
    
    