from datetime import datetime

class FOOD:
    def __init__(self, name, proteins, carbs, fats,insertion_date=None,calories=None):
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
