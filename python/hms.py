patients = {}

def add_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        print("Patient ID already exists.")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    patients[pid] = {
        'name': name,
        'age': age,
        'gender': gender,
        'appointments': [],
        'reports': []
    }
    print("Patient added successfully.")

def view_patient():
    pid = input("Enter Patient ID: ")
    patient = patients.get(pid)
    if not patient:
        print("Patient not found.")
        return
    print(f"\nPatient ID: {pid}")
    print(f"Name: {patient['name']}")
    print(f"Age: {patient['age']}")
    print(f"Gender: {patient['gender']}")
    print("Appointments:")
    for app in patient['appointments']:
        print(f" - {app}")
    print("Reports:")
    for report in patient['reports']:
        print(f" - {report}")

def book_appointment():
    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("Patient not found.")
        return
    date = input("Enter Appointment Date (DD-MM-YYYY): ")
    doctor = input("Enter Doctor Name: ")
    appointment = f"{date} with Dr. {doctor}"
    patients[pid]['appointments'].append(appointment)
    print("Appointment booked.")

def add_report():
    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("Patient not found.")
        return
    report = input("Enter Report Info: ")
    patients[pid]['reports'].append(report)
    print("Report added.")

def view_all_patients():
    if not patients:
        print("No patients found.")
        return
    print("\nAll Patients:")
    for pid, data in patients.items():
        print(f"ID: {pid}, Name: {data['name']}, Age: {data['age']}, Gender: {data['gender']}")

def main():
    while True:
        print("\nHOSPITAL MANAGEMENT SYSTEM")
        print("1. Add Patient")
        print("2. View Patient Details")
        print("3. Book Appointment")
        print("4. Add/View Reports")
        print("5. View All Patients")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patient()
        elif choice == '3':
            book_appointment()
        elif choice == '4':
            add_report()
        elif choice == '5':
            view_all_patients()
        elif choice == '6':
            print("Exiting System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
