from linkedlist import LinkedList
from doublylinkedlist import DoublyLinkedList
from stack import Stack
from queu import Queue

#Class Hospital System to manage the whole system
class HospitalManagementSystem:
    def __init__(self):
        self.patients = DoublyLinkedList()     #Call DoublyLinkList to add patients
        self.doctors = DoublyLinkedList()      #Call DoublyLinkList to add doctors
        self.prescriptions = Stack()           #Call Stack to add prescriptions
        self.consultation_queue = Queue()      #Call queue for consultation
        self.prescription_id_counter = 0

    #Add patient in system using patient class
    def add_patient(self, patient):
        self.patients.append(patient)

    #Add doctor in system using doctor class
    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    #Update existing record of patient 
    def update_patient_record(self, patient_id, new_name=None, new_age=None, new_admission_date=None, new_condition=None):
        current = self.patients.head
        while current:
            if current.data.id == patient_id:        #use condition to match the patient id
                if new_name is not None:
                    current.data.name = new_name     #update name of patient
                if new_age is not None:
                    current.data.age = new_age       #update age
                if new_admission_date is not None:       
                    current.data.admission_date = new_admission_date       #update admission date
                if new_condition is not None:
                    current.data.condition = new_condition          #update condition
                return True
            current = current.next
        return False

    #update doctor existing record
    def update_doctor_record(self, doctor_id, new_name, new_experience, new_specialization):
        current = self.doctors.head
        while current:
            if current.data.id == doctor_id:        #use condition to match doctor id
                if new_name:
                    current.data.name = new_name     #update name of doctor
                if new_specialization:
                    current.data.specialization = new_specialization   #update doctor specialization 
                if new_experience:
                    current.data.experience = new_experience       #update doctor experience
                return True
            current = current.next
        return False

    #remove patient record by using patient class
    def remove_patient_record(self, patient_id):
        return self.patients.remove(patient_id)

    #remove doctor record using doctor class
    def remove_doctor_record(self, doctor_id):
        return self.doctors.remove(doctor_id)

    #View all patients record in Hospital
    def view_all_patients(self):
        current = self.patients.head

        #use loop to print details 
        while current:
            print()
            print("ID:", current.data.id)
            print("Name:", current.data.name)
            print("Age:", current.data.age)
            print("Admission Date:", current.data.admission_date)
            print("Condition:", current.data.condition)
            current = current.next

    #Function to show detail of patients
    def summary_of_patient(self, patient_id):
        current_patient = self.patients.head

        #use loop to show details
        while current_patient:
            if current_patient.data.id == patient_id:
                print()     
                print("Patient ID:", current_patient.data.id)
                print("Name:", current_patient.data.name)
                print("Age:", current_patient.data.age)
                print("Condition:", current_patient.data.condition)

                attending_doctor = None
                current_doctor = self.doctors.head

                #use loop to appoint doctor to patient
                while current_doctor:
                    consultation_queue = current_doctor.data.consultation_queue
                    for item in consultation_queue.items:
                        if item.id == patient_id:
                            attending_doctor = current_doctor.data
                            break
                    if attending_doctor:
                        break
                    current_doctor = current_doctor.next

                # Display attending doctor's information
                if attending_doctor:
                    print()
                    print("Attending Doctor:")
                    print("  ID:", attending_doctor.id)
                    print("  Name:", attending_doctor.name)
                    print("  Specialization:", attending_doctor.specialization)
                    print("  Experience:", attending_doctor.experience)
                else:
                    print("Attending Doctor: Not assigned")

                print()
                print("Prescriptions:")
                #Call stack here to store prescription record
                temp_stack = Stack() 
                found_prescription = False

                #Iterate loop when stack is not empty
                while not self.prescriptions.is_empty():
                    prescription = self.prescriptions.pop()     #pop the details from stack
                    if prescription["patient_id"] == patient_id:
                        found_prescription = True
                        print("  Prescription ID:", prescription["id"])
                        print("  Doctor ID:", prescription["doctor_id"])
                        print("  Doctor Name:", prescription["doctor_name"])
                        print("  Medication:", prescription["medication"])
                        print("  Dosage:", prescription["dosage"])
                        print("  Duration:", prescription["duration"])
                        print("  Notes:", prescription["notes"])
                    temp_stack.push(prescription)
                while not temp_stack.is_empty():
                    self.prescriptions.push(temp_stack.pop())

                if not found_prescription:
                    print("  No prescriptions found.")

                return
            current_patient = current_patient.next
        print("Patient not found.")

    #View all doctors present in Hospital
    def view_all_doctors(self):
        current = self.doctors.head
        while current:
            print()
            print("ID:", current.data.id)
            print("Name:", current.data.name)
            print("Experience:", current.data.experience)
            print("Specialization:", current.data.specialization)
            current = current.next

    #View all doctors consultation queue
    def view_all_doctors_queue(self):
        current_doctor = self.doctors.head
        while current_doctor:
            doctor = current_doctor.data
            doctor_id = doctor.id
            print()
            print("Consultation Queue for Doctor", doctor.name, "(ID:", doctor_id, ")")
            doctor.consultation_queue.display()    #use display function of queue class
            current_doctor = current_doctor.next

    #add patient for consultaion with doctor function
    def add_patient_for_specific_doctor_queue(self, patient_id, doctor_id):
        current_doctor = self.doctors.head
        while current_doctor:
            if current_doctor.data.id == doctor_id:     #match doctor id to assign patient 
                current_patient = self.patients.head
                while current_patient:
                    if current_patient.data.id == patient_id:       #match patient id to assign doctor
                        current_doctor.data.consultation_queue.enqueue(current_patient.data)   #use enqueue to add details in queue 
                        return True
                    current_patient = current_patient.next
                print("Patient not found.")
                return False
            current_doctor = current_doctor.next
        print("Doctor not found.")
        return False

    #remove patient from queue function
    def remove_patient_for_specific_doctor_queue(self, doctor_id, patient_id):
        current_doctor = self.doctors.head
        while current_doctor:
            if current_doctor.data.id == doctor_id:
                return current_doctor.data.remove_patient_from_consultation_queue(patient_id)  #use dequeue to remove details from queue
            current_doctor = current_doctor.next
        return False

    #Prescription removal from queue function
    def give_prescription(self, patient_id, prescription_info, doctor_id, doctor_name):
        if self.remove_patient_for_specific_doctor_queue(doctor_id, patient_id):
            print("Patient with ID " + str(patient_id) + " appointment is done with Dr. " + doctor_name)
            print("Patient removed from the consultation queue of Dr. " + doctor_name)
        else:
            print("Error: Patient not found in the consultation queue of the specified doctor.")

        #call generate prescription function to display prescription
        prescription_id = self.generate_prescription_id()
        prescription = {
            "id": prescription_id,
            "doctor_id": doctor_id,
            "doctor_name": doctor_name,
            "patient_id": patient_id,
            "medication": prescription_info["medication"],
            "dosage": prescription_info["dosage"],
            "duration": prescription_info["duration"],
            "notes": prescription_info["notes"]
        }

        #push function to add prescription in stack
        self.prescriptions.push(prescription)
        print("Prescription added successfully.")
        return prescription_id

    #prescription id assignment function
    def generate_prescription_id(self):
        self.prescription_id_counter += 1
        return self.prescription_id_counter

    #View all prescriptions in LIFO for all doctors function
    def view_all_prescriptions_for_all_doctors(self):
        print("All Doctors Prescription in Stack Order Last-In-First-Out:")
        print()
        temp_stack = Stack()   #call stack class here

        #check the stack is empty or not
        while not self.prescriptions.is_empty():
            prescription = self.prescriptions.pop()
            #print the details of prescription 
            print("Prescription ID:", prescription["id"])
            print("Doctor ID:", prescription["doctor_id"])
            print("Doctor Name:", prescription["doctor_name"])
            print("Patient ID:", prescription["patient_id"])
            print("Medication:", prescription["medication"])
            print("Dosage:", prescription["dosage"])
            print("Duration:", prescription["duration"])
            print("Notes:", prescription["notes"])
            print()
            temp_stack.push(prescription)
        while not temp_stack.is_empty():
            self.prescriptions.push(temp_stack.pop())

    #View prescription of patient by his id function
    def view_prescription_by_patient_id(self, patient_id):
        print()
        print("Prescriptions for Patient ID:", patient_id)
        found_prescription = False
        temp_stack = Stack()  
        while not self.prescriptions.is_empty():
            prescription = self.prescriptions.pop()
            #condition to check patient id and then print its details
            if prescription["patient_id"] == patient_id:
                print("Prescription ID:", prescription["id"])
                print("Doctor ID:", prescription["doctor_id"])
                print("Doctor Name:", prescription["doctor_name"])
                print("Medication:", prescription["medication"])
                print("Dosage:", prescription["dosage"])
                print("Duration:", prescription["duration"])
                print("Notes:", prescription["notes"])
                found_prescription = True
            temp_stack.push(prescription)
        while not temp_stack.is_empty():
            self.prescriptions.push(temp_stack.pop())
        if not found_prescription:
            print("No prescriptions found for Patient ID:", patient_id)

    #view prescription by doctor id function
    def view_prescription_by_doctor_id(self, doctor_id):
        print()
        print("Prescriptions for Doctor ID:", doctor_id)
        found_prescription = False
        temp_stack = Stack()  
        while not self.prescriptions.is_empty():
            prescription = self.prescriptions.pop()
            if prescription["doctor_id"] == doctor_id:
                print("Prescription ID:", prescription["id"])
                print("Patient ID:", prescription["patient_id"])
                print("Medication:", prescription["medication"])
                print("Dosage:", prescription["dosage"])
                print("Duration:", prescription["duration"])
                print("Notes:", prescription["notes"])
                found_prescription = True
            temp_stack.push(prescription)
        while not temp_stack.is_empty():
            self.prescriptions.push(temp_stack.pop())
        if not found_prescription:
            print("No prescriptions found for Doctor ID:", doctor_id)

