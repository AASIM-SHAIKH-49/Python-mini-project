#Q5:DICTIONARIES+FUNCTION+CONTROL STUCTURE
#WRITING A FUNCTION STUDENT_DATABSE THAT USES A DICTIONARY(ROLL NUMBER AS KEY) TOSTORE STUDENT RECORDS
#SHOWCASING A MENU IN A LOOP
#Q5:DICTIONARIES+FUNCTION+CONTROL STUCTURE
#WRITING A FUNCTION STUDENT_DATABSE THAT USES A DICTIONARY(ROLL NUMBER AS KEY) TOSTORE STUDENT RECORDS
#SHOWCASING A MENU IN A LOOP
def student_database():
    students={}
    while True:
        print("1.ADD STUDENT")
        print("2.SEARCH STUDENT")
        print("2.DISPLAY ALL")

        choice=int(input("ENTER THE OPERATION NUMBER")) #GAINING CHOICE
        if choice==1:
            roll_no=int(input("ENTER STUDENT ROLL NUMBER:"))
            name=input("PLEASE ENTER NAME OF STUDENT:")
            age=int(input("ENTER THA AGE OF STUDENT:"))
            students.update({roll_no:{
                "NAME":name,
                "AGE":age,
                "ROLL NUMBER":roll_no
            }})
            print("STUDENT ADDED SUCCESSFULLY")
        elif choice==2:
            roll_s=int(input("ENTER THE ROLL NUMBER OF STUDENT WHOM TO SEARCH:"))
            student=students.get(roll_s)
            if student:
                 print("STUDENT NAME:",student["NAME"])
                 print("STUDENT AGE:",student["AGE"])
                 print("STUDENT ROLL NUMBER:",student["ROLL NUMBER"])
            
           
            
        elif choice==3:
            if len(students)==0:
                print("NO STUDENT AVAILABLE")
            else:
                print("/nSTUDENT RECORDS")
                for roll_no,details in students.items():
                    print("ROLL NUMBER:",roll_no)
                    print("ROLL NUMBER:",details["NAME"])
                    print("ROLL NUMBER:",details["AGE"])
        elif choice==4:
            print("EXITING")
            break
            

student_database()

        


