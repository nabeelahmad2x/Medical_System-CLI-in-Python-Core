from datetime import datetime

import re
import bcrypt

from mymodels import Patient, Doctor, Medical_History, Medicine, Appointment, Encounter, Payment_History

#lists to store data on runtime..
patient_list = list()
doctor_list = list()
appointments_list = list()
encounters_list = list()
medicine_list = list()
payment_list = list()
medical_history_list = list()


# CLI FUNCTIONS..
def home_cli():
    while True:
        email = input("Username/Email: ")
        password = input("Password: ")

        if login(email, password):
            pass
        else:
            print("Invalid Credentials. Try Again.")

def doctors_system(doctor_id):
    print("""\t1. Show All Appointments.
          2. Logout
          0. Exit""")
    while True:
        user_input = int(input("Input: "))
        if user_input == 0:
            break
        elif user_input == 1:
            print("Printing appointments info..")
            print_appointment_info(doctor_id)
        elif user_input == 2:
            print("LOG OUT..")
            home_cli()
        else:
            print("INVALID INPUT.")

def admin_system():
    print("""\t1. Add Doctor.
          2. Add Patient.
          3. Add Appointment.
          4. Add Encounter.
          5. Add Medicine.
          6. Add Payment History.
          7. Show Encounter info
          8. Show Appointment info
          9. Show Patient info
          10. Show Doctor info""")
    while True:
        user_input = int(input("Input: "))

        if user_input == 0:
            break
        elif user_input == 1:
            add_doctor()
        elif user_input == 2:
            add_patient()
        elif user_input == 3:
            add_appointment()
        elif user_input == 4:
            add_encounter()
        elif user_input == 5:
            add_medicine()
        elif user_input == 6:
            add_payment()
        elif user_input == 7:
            print_encounter_info(input("Encounter number:"))
        elif user_input == 8:
            print_appointment_info(input("Appointment number:"))
        elif user_input == 9:
            print_patient_info(int(input("Patient ID:")))
        elif user_input == 10:
            print_doctor_info(int(input("Doctor ID:")))
        else:
            print("Invalid Input.")  


# LOGIN & AUTHENTICATION..
def authenticate(email, password):
    global doctor_list
    
    for i in range(len(doctor_list)):
        if doctor_list[i].email == email:
            key = doctor_list[i].password[:29]
            password = bcrypt.hashpw(password.encode(), key)

            if doctor_list[i].password == password:
                return True
    else:
        return False


def login(email, password):
    global doctor_list
    if authenticate(email, password):
        for i in range(len(doctor_list)):
            if doctor_list[i].email == email and doctor_list[i].name == 'admin':
                admin_system()
            else:
                doctors_system(doctor_list[i].id)
    else:
        return False
        

def fetch_data_from_files():
    pass

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if(re.fullmatch(regex, email)):
        return True 
    else:
       return False

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password




# FOR ADMIN
def add_patient():
    global patient_list

    # INPUTS
    id = len(patient_list) + 1
    name = input("Name: ")
    contact = input("Contact: ")

    #email input + validation
    while True:
        email = input("Email: ")
        if validate_email(email):
            break
        else:
            print("Invalid Email. Enter again.")
    

    date_of_birth = input("Date of birth(yyyy/mm/dd): ")
    date_of_birth = datetime.strptime(date_of_birth, '%Y/%m/%d')

    blood_group = input("Blood group: ")
    disease_stage = input("Disease stage: ")

    # creating object and storing in list 
    patient = Patient(id, name, contact, email, date_of_birth, blood_group, disease_stage)
    patient_list.append(patient)

    print(f"Patient added at index: {len(patient_list)}")
    print(patient)

def add_doctor():
    global doctor_list

    # INPUTS
    id = len(doctor_list) + 1
    name = input("Name: ")
    contact = input("Contact: ")    
    
    #email input + validation
    while True:
        email = input("Email: ")
        if validate_email(email):
            break
        else:
            print("Invalid Email. Enter again.")

    password = input("Set Password: ")
    password = hash_password(password)
    
    date_of_birth = input("Date of birth(yyyy/mm/dd): ")
    date_of_birth = datetime.strptime(date_of_birth, '%Y/%m/%d')

    designation = input("Designation: ")
    speciality = input("Speciality: ")
    active_status = input("Active Status: ")

    # creating object and storing in list 
    doctor = Doctor(id, name, contact, email, password, date_of_birth, designation, speciality, active_status)    
    doctor_list.append(doctor)

    print(f"Doctor ID: {len(doctor_list)}")
    print(doctor)

def add_medicine():
    global medicine_list
    name = input("Name: ")
    purpose = input("Purpose of medicine: ")
    formula = input("Formula of medicine: ")
    
    medicine = Medicine(name, purpose, formula)
    medicine_list.append(medicine)
    
    print(f"Medcine added at index: {len(medicine_list)}")

def add_appointment():
    global appointments_list

    appointment_id = len(appointments_list) + 1
    doctor_id = input("Doctor ID: ")
    patient_id = input("Patient ID: ")
    appointment_date = input("Date: ")
    appointment_time = input("Time: ")
    status = input("Status: ")

    appointment = Appointment(appointment_id, doctor_id, patient_id, appointment_date, appointment_time, status)
    appointments_list.append(appointment)
    
    print(f"Appointment added at: {len(appointments_list)}")
    print(f"Details: {appointment}")

def add_encounter():
    global encounter_list

    encounter_id = len(encounters_list) + 1
    datetime = input("date: ")
    appointment_id = int(input("Enter Appoinment ID: "))
    patient_name = input("Enter Patient Name: ")
    doctor_name = input("Enter Doctor Name: ")
    
    encounter = Encounter(encounter_id, appointment_id, patient_name, doctor_name, datetime)
    encounters_list.append(encounter)
    print(f"Encounter Saved at index: {len(encounters_list)}")
    
def add_payment():
    global payment_list
    payment_id = len(payment_list) + 1
    encounter_id = input("Encounter ID: ")    #check if encounter with same id is present or not..
    total_fee = input("Medical Fee: ")
    payment_status = input("Payment Status:")
    
    payment =  Payment_History(payment_id, encounter_id, total_fee, payment_status)
    payment_list.append(payment)
    
    print(f"Payment info added at index: {len(payment_list)}")

def add_medical_history():
    global medical_history_list

    id = len(medical_history_list) + 1
    medications = input("Any Regular Medications: ")
    surgeries = input("Past Surgeries: ")
    allergies = input("Allergies: ")
    health_conditions = input("Health conditions: ")

    medical_history = Medical_History(id,medications, surgeries, allergies, health_conditions)
    medical_history_list.append(medical_history)

    print("Info Saved.")
    

def print_appointment_info(id):
    global appointments_list
    for i in range(len(appointments_list)):
        if appointments_list[i].appointment_id == id:
            print(appointments_list[i])

def print_patient_info(patient_id):
    global patient_list

    for i in range(len(patient_list)):
        if patient_list[i].id == patient_id:
            patient = patient_list[i]

            print(patient)
            print(f"Age: {calculate_age(patient.date_of_birth)}")

def print_doctor_info(doctor_id):
    global doctor_list
    for i in range(len(doctor_list)):
        if doctor_list[i].id == doctor_id:
            doctor = doctor_list[i]

            print(doctor)
            print(f"Age: {calculate_age(doctor.date_of_birth)}")

def print_encounter_info(encounter_id):
    global encounters_list
    
    for i in range(len(encounters_list)):
        if encounters_list[i].encounter_id == encounter_id:
            encounter = encounters_list[i]
            print(encounter)
    
    print_appointment_info(encounter.encounter_appointment_id)
    print_patient_info(encounter.encounter_patient_name)
    print_doctor_info(encounter.encounter_doctor_name)
