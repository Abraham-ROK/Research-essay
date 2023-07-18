from datetime import datetime
import uuid

class FOOD:
    def __init__(self,  name, proteins, carbs, fats, id=None, insertion_date=None,calories=None):
        self.id = id 
        self.name = name
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
        self.insertion_date = insertion_date
        self.calories = calories

    @property
    def set_calories(self):
        return float(self.proteins) * 4 + float(self.carbs) * 4 + float(self.fats) * 9
    
    @property
    def set_date(self):
        return datetime.now()
    
    
    def set_id(self):
        return str(uuid.uuid4())
    
    
    def get_id(self):
        return self.id