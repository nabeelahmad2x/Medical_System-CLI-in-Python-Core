from mymodels import Patient, Doctor, Medical_History, Medicine, Appointment, Encounter, Payment_History

#lists to store data on runtime..
patient_list = list()
doctor_list = list()
appointments_list = list()
encounters_list = list()
medicine_list = list()
payment_list = list()
medical_history_list = list()


def add_patient():
    global patient_list

    name = input("Name: ")
    contact = input("Contact: ")
    email = input("Email: ")
    date_of_birth = input("Date of birth(yyyy/mm/dd): ")
    blood_group = input("Blood group: ")
    disease_stage = input("Disease stage: ")

    
    patient = Patient(name, contact, email, date_of_birth, blood_group, disease_stage)
    patient_list.append(patient)

    print(f"Patient added at index: {len(patient_list)}")
    print(patient)

def add_doctor():
    global doctor_list

    name = input("Name: ")
    contact = input("Contact: ")
    email = input("Email: ")
    date_of_birth = input("Date of birth(yyyy/mm/dd): ")
    designation = input("Designation: ")
    speciality = input("Speciality: ")
    active_status = input("Active Status: ")

    doctor = Doctor(name, contact, email, date_of_birth, designation, speciality, active_status)    
    doctor_list.append(doctor)

    print(f"Doctor added at index: {len(doctor_list)}")
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
    date = input("Date: ")
    time = input("Time: ")
    venue = input("Venue: ")

    appointment = Appointment(appointment_id, date, time, venue)
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

def print_patient_info(patient_name):
    global patient_list
    for i in range(len(patient_list)):
        if patient_list[i].name == patient_name:
            print(patient_list[i])

def print_doctor_info(doctor_name):
    global doctor_list
    for i in range(len(doctor_list)):
        if doctor_list[i].name == doctor_name:
            print(doctor_list[i])

def print_encounter_info(encounter_id):
    global encounters_list
    
    for i in range(len(encounters_list)):
        if encounters_list[i].encounter_id == encounter_id:
            encounter = encounters_list[i]
            print(encounter)
    
    print_appointment_info(encounter.encounter_appointment_id)
    print_patient_info(encounter.encounter_patient_name)
    print_doctor_info(encounter.encounter_doctor_name)

    