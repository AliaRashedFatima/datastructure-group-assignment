#Patient class to add patient details
class Patient:
    def __init__(self, id, name, age, condition, admission_date):
        self.id = id
        self.name = name
        self.age = age
        self.condition = condition
        self.admission_date = admission_date
        self.appointment = None