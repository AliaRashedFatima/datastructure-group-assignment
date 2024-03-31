from hospitalsystem import HospitalManagementSystem
from patient import Patient
from doctor import Doctor

#call main function
if __name__ == "__main__":
    #call HospitalmanagemnetSystem class
    hospital = HospitalManagementSystem()

    #loop to print the menu driven interface
    while True:
        print("............... $$$Hospital System$$$ ...............")
        print("...............1: Hospital Management................")
        print("...............2: Manage Consultation................")
        print("...............3: Prescription.......................")
        print("...............4: Exit...............................")

        choice = input("Enter your choice: ")

        #different if else used here for different options and different menus 
        if choice == "1":
            while True:
                print()
                print("A. ADD PATIENT IN RECORD")
                print("B. ADD DOCTOR RECORD")
                print("C. UPDATE PATIENT RECORD")
                print("D. UPDATE DOCTOR RECORD")
                print("E. REMOVE PATIENT RECORD")
                print("F. REMOVE DOCTOR RECORD")
                print("G. VIEW ALL PATIENTS")
                print("H. SUMMARY OF PATIENT")
                print("I. VIEW ALL DOCTORS")
                print("J. VIEW ALL DOCTORS QUEUE")
                print("K. ADD PATIENT FOR SPECIFIC DOCTOR QUEUE")
                print("L. REMOVE PATIENT FOR SPECIFIC DOCTOR QUEUE")
                print("M. EXIT")

                sub_choice = input("Enter your choice: ").lower()

                if sub_choice == "a":
                    id = input("Enter patient ID: ")
                    name = input("Enter patient name: ")
                    age = input("Enter patient age: ")
                    condition = input("Enter patient condition: ")
                    admission_date = input("Enter admission date (YYYY-MM-DD): ")
                    patient = Patient(id, name, age, condition, admission_date)  #call Patient class to add details 
                    hospital.add_patient(patient)   #add patient function to add patient
                    print("Patient added successfully.")
                    pass

                elif sub_choice == "b":
                    id = input("Enter doctor ID: ")
                    name = input("Enter doctor name: ")
                    experience = input("Enter experience in years:")
                    specialization = input("Enter doctor specialization: ")
                    doctor = Doctor(id, name, experience, specialization)    #call doctor class to add doctors
                    hospital.add_doctor(doctor)           #add doctor function to add doctor
                    print("Doctor added successfully.")
                    pass
                
                elif sub_choice == "c":
                    patient_id = input("Enter patient ID to update: ")
                    patient_found = False
                    current = hospital.patients.head
                    while current:
                        if current.data.id == patient_id:
                            patient_found = True
                            break
                        current = current.next

                    if patient_found:
                        new_name = input("Enter new name: ")
                        new_age = input("Enter new age: ")
                        new_admission_date = input("Enter new admission date (YYYY-MM-DD): ")
                        new_condition = input("Enter new condition: ")
                        #update patient record function to update existing record
                        if hospital.update_patient_record(patient_id, new_name, new_age, new_admission_date, new_condition):  
                            print("Patient record updated successfully.")
                        else:
                            print("Failed to update patient record.")
                    else:
                        print("Patient not found.")

                
                elif sub_choice == "d":
                    doctor_id = input("Enter doctor ID to update: ")
                    doctor_found = False
                    current = hospital.doctors.head
                    while current:
                        if current.data.id == doctor_id:
                            doctor_found = True
                            break
                        current = current.next

                    if doctor_found:
                        new_name = input("Enter new name: ")
                        new_specialization = input("Enter new specialization: ")
                        new_experience = input("Enter new experience in years:")

                        #update doctor record for existing doctor
                        if hospital.update_doctor_record(doctor_id, new_name, new_experience, new_specialization):
                            print("Doctor record updated successfully.")
                        else:
                            print("Failed to update doctor record.")
                    else:
                        print("Doctor not found.")

                
                elif sub_choice == "e":
                    patient_id = input("Enter patient ID to remove: ")

                    #remove patient record from system
                    if hospital.remove_patient_record(patient_id):
                        print("Patient record removed successfully.")
                    else:
                        print("Patient not found.")
                    pass
                
                elif sub_choice == "f":
                    doctor_id = input("Enter doctor ID to remove: ")
                    #remove doctor record from system
                    if hospital.remove_doctor_record(doctor_id):
                        print("Doctor record removed successfully.")
                    else:
                        print("Doctor not found.")
                    pass
                
                elif sub_choice == "g":
                    hospital.view_all_patients()     #view all patients record
                    pass
                
                elif sub_choice == "h":
                    patient_id = input("Enter patient ID for summary: ")
                    hospital.summary_of_patient(patient_id)   #view all details of patients
                    pass
                
                elif sub_choice == "i":
                    hospital.view_all_doctors()     #view all doctors record
                    pass
                
                elif sub_choice == "j":
                    hospital.view_all_doctors_queue()       #view doctors queue
                    pass
                        
                elif sub_choice == "k":
                    print()
                    print("Doctors in the hospital:")
                    hospital.view_all_doctors()

                    print()
                    print("All Patients in the hospital:")
                    hospital.view_all_patients()

                    patient_id = input("Enter patient ID: ")
                    doctor_id = input("Enter doctor ID: ")

                    doctor_found = False
                    current_doctor = hospital.doctors.head
                    while current_doctor:
                        if current_doctor.data.id == doctor_id:
                            doctor_found = True
                            break
                        current_doctor = current_doctor.next

                    if doctor_found:
                        patient_found = False
                        current_patient = hospital.patients.head
                        while current_patient:
                            if current_patient.data.id == patient_id:
                                patient_found = True
                                break
                            current_patient = current_patient.next

                        if patient_found:
                            if hospital.add_patient_for_specific_doctor_queue(patient_id, doctor_id):   #add patient for appointed doctor queue
                                print("Patient added to doctor queue successfully.")
                            else:
                                print("Failed to add patient to doctor queue.")
                        else:
                            print("Patient not found.")
                    else:
                        print("Doctor not found.")

                
                elif sub_choice == "l":
                    doctor_id = input("Enter doctor ID: ")
                    patient_id = input("Enter patient ID: ")

                    if hospital.remove_patient_for_specific_doctor_queue(doctor_id, patient_id):   #remove patient from queue when appointment is done
                        print("Patient", patient_id, "removed from Doctor with id ", doctor_id, " and also removed from queue successfully {Appointment canceled}.")
                    else:
                        print("No patient is in the system with ID", patient_id, "in the queue for Doctor", doctor_id)
                
                elif sub_choice == "m":
                    break

                else:
                    print("Wrong Option (Try Again)")

        elif choice == "2":
            doctor_id = input("Enter doctor ID to obtain the consultation room: ")

            current_doctor = hospital.doctors.head
            while current_doctor:
                if current_doctor.data.id == doctor_id:
                    print("Consultation room obtained by Doctor:")
                    print("ID:", current_doctor.data.id)
                    print("Name:", current_doctor.data.name)
                    print("Specialization:", current_doctor.data.specialization)
                    print("Experience:", current_doctor.data.experience)
                    break
                current_doctor = current_doctor.next
            else:
                print("Doctor not found.")

            doctor_id = current_doctor.data.id
            doctor_name = current_doctor.data.name

            #menu for Manage Consultations 
            while True:
                print("............. $$$Manage Consultation$$$ .............")
                print("A. View Patient Detail by ID")
                print("B. Update Patient Condition")
                print("C. Recommend Another Doctor (Transfer)")
                print("D. Give Prescription")
                print("E. Exit")

                sub_choice = input("Enter your choice: ").lower()

                if sub_choice == "a":
                    patient_id = input("Enter patient ID: ")
                    hospital.summary_of_patient(patient_id)    #Summary of patients 

                elif sub_choice == "b":
                    patient_id = input("Enter patient ID: ")
                    new_condition = input("Enter new condition: ")
                    if hospital.update_patient_record(patient_id, new_condition=new_condition):
                        print("Patient condition updated successfully.")
                    else:
                        print("Failed to update patient condition because id not found")

                elif sub_choice == "c":
                    patient_id = input("Enter patient ID: ")
                    current_doctor_id = input("Enter current doctor ID: ")
                    new_doctor_id = input("Enter ID of the doctor to recommend: ")
                    if hospital.remove_patient_for_specific_doctor_queue(current_doctor_id, patient_id):
                        if hospital.add_patient_for_specific_doctor_queue(patient_id, new_doctor_id):
                            print("Patient transferred successfully to Doctor with ID", new_doctor_id)
                            print("Removed from first doctor queue and the patient to next doctor queue")
                        else:
                            print("Failed to transfer patient.")
                    else:
                        print("Patient not found or not assigned to the current doctor.")

                elif sub_choice == "d":
                    patient_id = input("Enter patient ID: ")
                    medication = input("Enter prescribed medication: ")
                    dosage = input("Enter dosage: ")
                    duration = input("Enter duration: ")
                    notes = input("Enter any additional notes: ")

                    prescription_info = {
                        "medication": medication,
                        "dosage": dosage,
                        "duration": duration,
                        "notes": notes
                    }

                    hospital.give_prescription(patient_id, prescription_info, doctor_id, doctor_name)   #add prescription for patient

                elif sub_choice == "e":
                    break

                else:
                    print("Wrong Option (Try Again)")

        elif choice == "3":
            while True:
                print()
                print("A: VIEW ALL PRESCRIPTIONS FOR ALL DOCTORS")
                print("B: VIEW PRESCRIPTION BY PATIENT ID")
                print("C: VIEW PRESCRIPTION BY DOCTOR ID")
                print("D: EXIT")

                sub_choice = input("Enter your choice: ").lower()

                if sub_choice == "a":
                    #view all prescriptions for all doctors
                    hospital.view_all_prescriptions_for_all_doctors()
                    pass

                elif sub_choice == "b":
                    patient_id = input("Enter patient ID: ")
                    hospital.view_prescription_by_patient_id(patient_id)
                    pass
                
                elif sub_choice == "c":
                    doctor_id = input("Enter doctor ID: ")
                    hospital.view_prescription_by_doctor_id(doctor_id)
                    pass
                
                elif sub_choice == "d":
                    break
                
                else:
                    print("Wrong Option (Try Again)")

        elif choice == "4":
            print("........... $$$ Exit Hospital System $$$ ...........")
            break

        else:
            print("Wrong Option (Try Again)")