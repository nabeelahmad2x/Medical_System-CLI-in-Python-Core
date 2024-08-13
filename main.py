from views import add_doctor, add_appointment, add_medicine, add_encounter, add_patient, add_payment, print_encounter_info, print_appointment_info, print_doctor_info, print_patient_info


def medical_system():
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


#id in Person
#calculate age based on birthday 
#email auth
#add doctor id to appointment
#add status to appointment(completed, not completed)


medical_system()