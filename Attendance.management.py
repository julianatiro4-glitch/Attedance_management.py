#========================================
# ATTENDANCE MANAGEMENT SYSTEM
#========================================

class AttendanceRecord:

    def __init__(self, student_name, course, year_level, date, status):

        self.__student_name = student_name.title()
        self.__course = course.upper()
        self.__year_level = year_level
        self.__date = date
        self.__status = status.capitalize()

    # GETTERS
    def get_student_name(self): return self.__student_name
    def get_course(self): return self.__course
    def get_year_level(self): return self.__year_level
    def get_date(self): return self.__date
    def get_status(self): return self.__status

    def display_record(self):
        print("--------------------------------")
        print(f"Name        : {self.__student_name}")
        print(f"Course      : {self.__course}")
        print(f"Year Level  : {self.__year_level}")
        print(f"Date        : {self.__date}")
        print(f"Status      : {self.__status}")
        print("--------------------------------")


#========================================
# SYSTEM CLASS
#========================================
class AttendanceSystem:

    def __init__(self):

        self.teacher_username = "teacher"
        self.teacher_password = "1234"

        self.records = []

        # STUDENT DATABASE (NAME-BASED)
        self.students = {
            "Alice": {"course": "BSIT", "year_level": "1"},
            "Bob": {"course": "BSCS", "year_level": "2"}
        }

    #========================================
    # STUDENT LOGIN
    #========================================
    def student_login(self):

        print("\n========== STUDENT LOGIN ==========")

        student_name = input("Enter Student Name: ").strip().title()

        if student_name not in self.students:
            print("Student not found in system!\n")
            return

        print(f"\nWelcome {student_name}!")
        self.student_menu(student_name)

    #========================================
    # TEACHER LOGIN
    #========================================
    def teacher_login(self):

        print("\n========== TEACHER LOGIN ==========")

        user = input("Username: ")
        pw = input("Password: ")

        if user == self.teacher_username and pw == self.teacher_password:
            print("Teacher Login Successful!\n")
            self.teacher_menu()
        else:
            print("Invalid Credentials!\n")

    #========================================
    # REGISTER STUDENT
    #========================================
    def register_student(self):

        print("\n========== STUDENT REGISTRATION ==========")

        name = input("Enter Student Name: ").strip().title()

        if name in self.students:
            print("Student already exists!\n")
            return

        course = input("Enter Course: ").strip()
        year = input("Enter Year Level: ").strip()

        self.students[name] = {
            "course": course,
            "year_level": year
        }

        print("Student Registered Successfully!\n")

    #========================================
    # MARK ATTENDANCE (NO REPETITION)
    #========================================
    def mark_attendance(self):

        print("\n========== MARK ATTENDANCE ==========")

        student_name = input("Enter Student Name: ").strip().title()

        if student_name not in self.students:
            print("Student not found! Please register first.\n")
            return

        student = self.students[student_name]

        date = input("Enter Date (YYYY-MM-DD): ")

        while True:
            status = input("Status (Present/Absent/Late): ").capitalize()
            if status in ["Present", "Absent", "Late"]:
                break
            print("Invalid Status!")

        record = AttendanceRecord(
            student_name,
            student["course"],
            student["year_level"],
            date,
            status
        )

        self.records.append(record)

        print("Attendance Recorded Successfully!\n")

    #========================================
    # VIEW ALL ATTENDANCE
    #========================================
    def view_attendance(self):

        print("\n========== ALL ATTENDANCE ==========")

        if not self.records:
            print("No records found.\n")
            return

        for r in self.records:
            r.display_record()

    #========================================
    # SEARCH ATTENDANCE
    #========================================
    def search_attendance(self):

        print("\n========== SEARCH ==========")

        name = input("Enter Student Name: ").strip().title()

        found = False

        for r in self.records:
            if r.get_student_name() == name:
                r.display_record()
                found = True

        if not found:
            print("No records found.\n")

    #========================================
    # STUDENT MENU
    #========================================
    def student_menu(self, student_name):

        while True:

            print("\n================================")
            print("|        STUDENT MENU          |")
            print("================================")
            print("| 1. View My Attendance        |")
            print("| 2. Logout                    |")
            print("================================")

            choice = input("Select: ")

            if choice == "1":

                found = False

                for r in self.records:
                    if r.get_student_name() == student_name:
                        r.display_record()
                        found = True

                if not found:
                    print("No attendance records yet.")

            elif choice == "2":
                break

    #========================================
    # TEACHER MENU
    #========================================
    def teacher_menu(self):

        while True:

            print("\n================================")
            print("|        TEACHER MENU          |")
            print("================================")
            print("| 1. Register Student          |")
            print("| 2. Mark Attendance           |")
            print("| 3. View All Attendance       |")
            print("| 4. Search Attendance         |")
            print("| 5. Logout                    |")
            print("================================")

            choice = input("Select: ")

            if choice == "1":
                self.register_student()

            elif choice == "2":
                self.mark_attendance()

            elif choice == "3":
                self.view_attendance()

            elif choice == "4":
                self.search_attendance()

            elif choice == "5":
                break

    #========================================
    # MAIN MENU
    #========================================
    def main_menu(self):

        while True:

            print("\n================================")
            print("| ATTENDANCE MANAGEMENT SYSTEM |")
            print("================================")
            print("| 1. Student Login             |")
            print("| 2. Teacher Login             |")
            print("| 3. Exit                      |")
            print("================================")

            choice = input("Select: ")

            if choice == "1":
                self.student_login()

            elif choice == "2":
                self.teacher_login()

            elif choice == "3":
                print("Exiting program...")
                break


#========================================
# RUN PROGRAM
#========================================
if __name__ == "__main__":
    system = AttendanceSystem()
    system.main_menu()