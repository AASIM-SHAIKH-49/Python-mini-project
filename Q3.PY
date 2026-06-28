#CREATING A MANAGE_MARKS() FUNCTION
try:
    def manage_marks():
        marks=[]  
        for i in range(5):
            mark=int(input("ENTER THE MARKS IN SUBJECT: "))  #TAKING FIVE SUBJJECT MARKS AS INPUT
            marks.append(mark)
        
    #CALCULATING HISHEST,LOWEST AND AVERAGE
        print("HIGHEST MARKS=",max(marks))
        print("LOWEST MARKS=",min(marks))
        print("AVERAGE=",sum(marks)/5)
    #sort in descending order
        print("REVERSED LIST=",marks.sort(reverse=True))
except ValueError:
    print("non-numeric terms not allowwded")

manage_marks()

     