import os

class HospitalManagementSystem:
    def __init__(self):
        self.data_dir = "data"
        self.files = {
            "patients": "patients.txt",
            "appointments": "appointments.txt",
            "billing": "billing.txt",
            "records": "records.txt",
            "reports": "report.txt"
        }
        self.departments = {
            "1": ("Cardiology", ["ECG", "Echocardiogram", "Cholesterol Test"]),
            "2": ("Neurology", ["EEG", "MRI Brain", "Nerve Conduction Study"]),
            "3": ("Orthopedics", ["X-Ray", "Bone Density Test", "MRI Spine"]),
            "4": ("Dermatology", ["Skin Biopsy", "Allergy Test", "Dermoscopy"]),
            "5": ("General Medicine", ["CBC", "Urine Test", "Blood Pressure Monitoring"]),
        }
        self.ensure_data_dir()

    def ensure_data_dir(self):
        os.makedirs(self.data_dir, exist_ok=True)
        for file in self.files.values():
            open(os.path.join(self.data_dir, file), "a").close()

    def register_patient(self):
        name = input("Enter patient's name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        contact = input("Enter contact number: ")
        patient_id = f"P{hash(name + contact) % 10000}"
        
        record = f"{patient_id},{name},{age},{gender},{contact}\n"
        with open(os.path.join(self.data_dir, self.files["patients"]), "a") as file:
            file.write(record)

        print(f"Patient registered with ID: {patient_id}")

    def view_patients(self):
        with open(os.path.join(self.data_dir, self.files["patients"]), "r") as file:
            print("\n===== Registered Patients =====")
            for line in file:
                print(line.strip())

    def book_appointment(self):
        patient_id = input("Enter Patient ID: ")
        print("Choose Department:")
        for key, (dept, _) in self.departments.items():
            print(f"{key}. {dept}")
        dept_choice = input("Enter department number: ")

        if dept_choice not in self.departments:
            print("Invalid department selected.")
            return

        department, recommended_tests = self.departments[dept_choice]
        doctor_name = input(f"Enter Doctor's Name (for {department}): ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        emergency = input("Is this an emergency? (yes/no): ")

        record = f"{patient_id},{doctor_name},{department},{date},{emergency}\n"
        with open(os.path.join(self.data_dir, self.files["appointments"]), "a") as file:
            file.write(record)

        print("Appointment booked successfully.")
        print(f"Recommended Tests from {department}:")
        for test in recommended_tests:
            print(f" - {test}")

        test_now = input("Do you want to conduct the tests now? (yes/no): ").strip().lower()
        if test_now == "yes":
            self.generate_report(patient_id, department, recommended_tests)

    def view_appointments(self):
        with open(os.path.join(self.data_dir, self.files["appointments"]), "r") as file:
            appointments = file.readlines()

        if not appointments:
            print("No appointments found.")
        else:
            print("\n===== List of Appointments =====")
            for appointment in appointments:
                patient_id, doctor_name, department, date, emergency = appointment.strip().split(",")
                print(f"Patient ID: {patient_id}, Doctor: {doctor_name}, Department: {department}, Date: {date}, Emergency: {emergency}")

    def generate_report(self, patient_id, department, tests):
        report_content = "Patient ID: " + patient_id + "\n"
        report_content += "Department: " + department + "\n"
        report_content += "Tests Conducted:\n"
        for test in tests:
            report_content += " - " + test + "\n"
        report_content += "-----------------------------\n"

        with open(os.path.join(self.data_dir, self.files["reports"]), "a") as file:
            file.write(report_content)
        print("Report saved successfully.")

    def view_reports(self):
        search_id = input("Enter Patient ID to view report: ")
        found = False
        with open(os.path.join(self.data_dir, self.files["reports"]), "r") as file:
            reports = file.read().split("-----------------------------\n")
            for report in reports:
                if f"Patient ID: {search_id}" in report:
                    print("\n===== Report Found =====")
                    print(report)
                    found = True
        if not found:
            print("No report found for this Patient ID.")

    def menu(self):
        while True:
            print("\n===== Hospital Management System =====")
            print("1. Register Patient")
            print("2. View Patients")
            print("3. Book Appointment")
            print("4. View Appointments")
            print("5. View Reports")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.register_patient()
            elif choice == "2":
                self.view_patients()
            elif choice == "3":
                self.book_appointment()
            elif choice == "4":
                self.view_appointments()
            elif choice == "5":
                self.view_reports()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    app = HospitalManagementSystem()
    app.menu()
