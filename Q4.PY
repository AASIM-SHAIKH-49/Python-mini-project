#Q4:OOPS CONCEPTS CREATING A CLASS WITH ATTRIBUTES

class student:
        def __init__(self,name,roll_no):
            self.name=name
            self.roll_no=roll_no
            self.marks_list=[]
        def add_mark(self,mark):
            if mark<0 or mark>100:
                raise ValueError("invalid marks")
            else:
                self.marks_list.append(mark)
        def get_average(self):
            if len(self.marks_list)==0:
                return
            else:
                return(sum(self.marks_list)/len(self.marks_list))
        def display(self):
            print("nam=".upper,self.name)
            print("ROLL NO=",self.roll_no)
            print("marks list".upper,self.marks_list)
            print("AVERAGE=",self.get_average())

try:
    name=input("ENTER NAME:")
    roll_no=int(input("ENTER ROLL NUMBER"))
    s=student(name,roll_no)

    for i in range(5):
        mark=float(input("enter marks"))
        s.add_mark(mark)
    #DISPLAYING
    s.display()

except ValueError as e:
    print("ERROR:",e)