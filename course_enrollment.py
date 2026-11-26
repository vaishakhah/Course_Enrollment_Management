import mysql.connector

class CourseEnrollment:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                user="root",
                host="localhost",
                password="VAISHAKHah@2005",
                database="course_enrollment"
            )
            print("Database Connected Successfully")
        except:
            print("Connection Failed")
    def Validate_Duration(self):
        while True:
            try:
                duration_months = int(input("Enter Duration Months: "))

                if duration_months > 0:
                    return duration_months
                else:
                    print("Duration must be greater than 0")
            except ValueError:
                print("Please enter a valid number")
    def Validate_Fee(self):
        while True:
            try:
                fee = int(input("Enter Fee: "))
                if fee > 0:
                    return fee
                else:
                    print("Fee must be greater than 0")
            except ValueError:
                print("Please enter a valid fee")
    def Enroll_Student(self,student_name,course_name,duration_months,enrollment_date,fee,status):
        try:
            cursor = self.con.cursor()
            query = "insert into enrollments(student_name,course_name,duration_months,enrollment_date,fee,status)values(%s,%s,%s,%s,%s,%s)"
            data = (student_name,course_name,duration_months,enrollment_date,fee,status)
            cursor.execute(query,data)
            self.con.commit()
            print("Student Enrolled Successfully")
        except:
            print("Failed to Enroll")
    def View_Enrollments(self):
        try:
            cursor = self.con.cursor()
            query = "select * from enrollments order by fee desc"
            cursor.execute(query)
            records = cursor.fetchall()
            if records:
                for rows in records:
                    print(rows)
            else:
                print("No Records Found")
        except:
            print("Failed to View Enrollments")
    def Search_Enrollment(self,enrollment_id):
        try:
            cursor = self.con.cursor()
            query = "select * from enrollments where enrollment_id=%s"
            data = (enrollment_id,)
            cursor.execute(query, data)
            record = cursor.fetchone()
            if record:
                print(record)
            else:
                print("No Record Found")

        except:
            print("Failed to Search Enrollment")

    def Update_Enrollment(self,enrollment_id,status,fee):
        try:
            cursor = self.con.cursor()
            query = " update enrollments set status =%s,fee =%s where enrollment_id =%s"
            data = (status,fee,enrollment_id)
            cursor.execute(query, data)
            self.con.commit()
            if cursor.rowcount > 0:
                print("Updated Successfully")
            else:
                print("No Records Found")
        except:
            print("Failed to Update:")
    def Delete_Enrollment(self, enrollment_id):
        try:
            cursor = self.con.cursor()
            query = "delete from enrollments where enrollment_id =%s"
            data = (enrollment_id,)
            cursor.execute(query, data)
            self.con.commit()
            if cursor.rowcount > 0:
                print("Deleted Successfully")
            else:
                print("No Record Found")
        except:
            print("Failed to Delete")
    def Enrollment_Summary(self):
        try:
            cursor = self.con.cursor()
            query1 = "select count(enrollment_id),sum(fee),avg(fee)from enrollments"
            cursor.execute(query1)
            record = cursor.fetchone()
            print("----- Financial SUMMARY -----")
            print("Total Enrollments:", record[0])
            print("Total Fee Collected:", record[1])
            print("Average Fee:", record[2])
            query2 = "select status, count(enrollment_id)from enrollments group by status"
            cursor.execute(query2)
            records = cursor.fetchall()
            for rows in records:
                print("Status:", rows[0], "| Students:", rows[1])
        except:
            print("Failed to Enrollment Summary")

obj = CourseEnrollment()

while True:
    print("_____MENU_____")
    print("1. Enroll Student")
    print("2. View All Enrollments")
    print("3. Search Enrollment")
    print("4. Update Enrollment Status")
    print("5. Delete Enrollment")
    print("6. Enrollment Summary")
    print("7. Exit")
    try:
        ch = int(input("Enter Your Choice (1-7): "))
    except ValueError:
        print("Please Enter a Valid Choice")
        continue
    if ch == 1:
        student_name = input("Enter Student Name: ")
        course_name = input("Enter Course Name: ")
        duration_months = obj.Validate_Duration()
        enrollment_date = input("Enter Enrollment Date: ")
        fee = obj.Validate_Fee()
        status = input("Enter Status: ")
        obj.Enroll_Student(student_name,course_name,duration_months,enrollment_date,fee,status)
    elif ch == 2:
        obj.View_Enrollments()
    elif ch == 3:
        enrollment_id = int(input("Enter Enrollment ID: "))
        obj.Search_Enrollment(enrollment_id)
    elif ch == 4:
        enrollment_id = int(input("Enter Enrollment ID to update: "))
        status = input("Enter New Status: ")
        fee = obj.Validate_Fee()
        obj.Update_Enrollment(enrollment_id, status, fee)
    elif ch == 5:
        enrollment_id = int(input("Enter Enrollment ID to Delete: "))
        obj.Delete_Enrollment(enrollment_id)
    elif ch == 6:
        obj.Enrollment_Summary()
    elif ch == 7:
        print("Thank you")
        exit()
    else:
        print("Invalid Choice")