from queu import Queue
#Doctor class to add doctor details
class Doctor:
    def __init__(self, id, name, experience, specialization):
        self.id = id
        self.name = name
        self.experience = experience
        self.specialization = specialization
        self.consultation_queue = Queue()  #use queue here to add data in queue for consultation

    #remove data of patient from queue function    
    def remove_patient_from_consultation_queue(self, patient_id):
        for patient in list(self.consultation_queue.items):
            if patient.id == patient_id:
                self.consultation_queue.items.remove(patient)   #use remove function of queue to remove details
                return True
        return False