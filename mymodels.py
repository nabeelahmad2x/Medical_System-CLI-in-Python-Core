from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id, name, contact, email, date_of_birth):
        self.id = id
        self.name = name
        self.contact = contact
        self.email = email
        self.date_of_birth = date_of_birth
 
    @abstractmethod
    def update_name(self):
        pass

    @abstractmethod
    def update_contact(self):
        pass

    @abstractmethod
    def update_email(self):
        pass


class Patient(Person):
    def __init__(self, id, name, contact, email, date_of_birth, blood_group, disease_stage):
        super().__init__(id, name, contact, email, date_of_birth)
        self.blood_group = blood_group
        self.disease_stage = disease_stage

    def __str__(self):
        return f"""Patient(ID: {self.id}, Name: {self.name}, Contact: {self.contact}, Email: {self.email},
               Date of Birth: {self.date_of_birth}, Blood Group: {self.blood_group},
               Disease Stage: {self.disease_stage})"""
    
    def update_name(self, new_name):
        self.name = new_name

    def update_contact(self, new_contact):
        self.contact = new_contact
    
    def update_email(self, new_email):
        self.email = new_email

    def update_disease_stage(self, updated_stage):
        self.disease_stage = updated_stage


class Doctor(Person):
    def __init__(self, id, name, contact, email, date_of_birth, designation, speciality, active_status):
        super().__init__(id, name, contact, email, date_of_birth)
        self.designation = designation
        self.speciality = speciality
        self.active_status = bool(active_status)
    
    def __str__(self):
        return f"""Doctor(ID: {self.id}, Name: {self.name}, Contact: {self.contact}, Email: {self.email},
               Date of Birth: {self.date_of_birth}, Designation: {self.designation}, 
               Speciality: {self.speciality}, Active Status: {self.active_status})"""
    
    def update_name(self, new_name):
        self.name = new_name

    def update_contact(self, new_contact):
        self.contact = new_contact
    
    def update_email(self, new_email):
        self.email = new_email

    def update_designation(self, new_designation):
        self.designation = new_designation
    
    def update_speciality(self, new_speciality):
        self.speciality = new_speciality
    
    def update_active_status(self, new_status):
        self.active_status = new_status


class Medicine:
    def __init__(self, name, purpose, formula):
        self.name = name
        self.purpose = purpose
        self.formula = formula
        
    def __str__(self):
        return f"Medicine Name: {self.name}, Purpose: {self.purpose}, formula: {self.formula}"


class Appointment:
    def __init__(self, id, doctor_id, patient_id, date, time, status):
        self.appointment_id = id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.appointment_date = date
        self.appointment_time = time
        self.status = status
    
    def __str__(self):
        return f"""Appointment ID: {self.appointment_id}, Doctor ID: {self.doctor_id}, 
        Patient ID: {self.patient_id}, Date & Time: {self.appointment_date}, {self.appointment_time},
        Venue: {self.venue}, Appointment Status: {self.status}"""
    

class Encounter:
    def __init__(self, encounter_id, appointment_id, patient_name, doctor_name, datetime):
        self.encounter_id = encounter_id
        self.encounter_appointment_id = appointment_id
        self.encounter_patient_name = patient_name
        self.encounter_doctor_name = doctor_name
        self.datetime = datetime
        self.notes = None
        self.prescription = None

    def __str__(self):
        return f"""Encounter(ID: {self.encounter_id}, Appointment ID: {self.encounter_appointment_id}, 
               Patient: {self.encounter_patient_name}, Doctor: {self.encounter_doctor_name}, Notes: {self.notes}, 
               DateTime: {self.datetime}, Prescription: {self.prescription})"""
    
    def update_notes(self, notes):
        self.notes = notes

    def update_prescription(self, prescription):
        self.prescription = prescription

class Payment_History:
    def __init__(self, id, encounter_id, total_fee, payment_status):
        self.id = id
        self.encounter_id = encounter_id
        self.total_fee = total_fee
        self.payment_status = payment_status        

    def __str__(self):
        return f"""PaymentHistory(ID: {self.id}, Encounter ID: {self.encounter_id},
               Total Fee: {self.total_fee}, Payment Status: {self.payment_status})"""

class Medical_History:
    def __init__(self, id, medications, surgeries, allergies, health_conditions):
        self.id = id
        self.medications = medications
        self.surgeries = surgeries
        self.allergies = allergies
        self.health_conditions = health_conditions

    def __str__(self):
        return f"""Medical History(ID: {self.id}, Current Medications: {self.medications},
               Surgeries: {self.surgeries}, allergies: {self.allergies},
               Health Conditions: {self.health_conditions})"""
    