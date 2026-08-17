import json
import os

class CollegeApplicationSystem:
    def __init__(self, filename="college_applications.json"):
        self.filename = filename
        self.applications = self.load_applications()

    def load_applications(self):
        """Loads existing applications from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_applications(self):
        """Saves current applications to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.applications, file, indent=4)

    def evaluate_admission(self, gpa, sat_act):
        """Determines admission status based on GPA and standardized test scores."""
        # Baseline criteria: GPA out of 4.0, SAT out of 1600
        if gpa >= 3.5 and sat_act >= 1300:
            return "Accepted (with Merit Scholarship)"
        elif gpa >= 3.0 and sat_act >= 1100:
            return "Accepted"
        elif gpa >= 2.5 and sat_act >= 950:
            return "Waitlisted"
        else:
            return "Rejected"

    def submit_application(self):
        """Collects student information and processes the application."""
        print("\n--- New College Application Form ---")
        name = input("Enter Student Full Name: ").strip()
        if not name:
            print("Name cannot be empty. Application aborted.")
            return

        email = input("Enter Email Address: ").strip()
        major = input("Intended Major/Program: ").strip()

        # Input validation for numerical scores
        try:
            gpa = float(input("Enter High School GPA (0.0 - 4.0): "))
            if not (0.0 <= gpa <= 4.0):
                print("Invalid GPA range. Must be between 0.0 and 4.0.")
                return

            sat_act = int(input("Enter SAT Score (400 - 1600): "))
            if not (400 <= sat_act <= 1600):
                print("Invalid SAT score. Must be between 400 and 1600.")
                return
        except ValueError:
            print("Invalid input format. Numeric values required for GPA and SAT.")
            return

        # Process Decision
        status = self.evaluate_admission(gpa, sat_act)

        # Store Application Record
        self.applications[email] = {
            "name": name,
            "major": major,
            "gpa": gpa,
            "sat_score": sat_act,
            "status": status
        }
        self.save_applications()
        
        print(f"\nSuccess! Application submitted for {name}.")
        print(f"Automated Admission Decision: **{status}**")

    def view_applications(self):
        """Displays all submitted college applications."""
        if not self.applications:
            print("\nNo applications found in the system.")
            return

        print("\n--- Submitted Applications List ---")
        for email, details in self.applications.items():
            print(f"\nStudent: {details['name']}")
            print(f"Email: {email}")
            print(f"Major: {details['major']}")
            print(f"GPA: {details['gpa']} | SAT: {details['sat_score']}")
            print(f"Decision Status: {details['status']}")
            print("-" * 35)

def main():
    system = CollegeApplicationSystem()
    
    while True:
        print("\n==== COLLEGE ADMISSION PORTAL ====")
        print("1. Submit New Application")
        print("2. View All Applications")
        print("3. Exit Portal")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            system.submit_application()
        elif choice == '2':
            system.view_applications()
        elif choice == '3':
            print("Exiting portal. Good luck with your admissions!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
