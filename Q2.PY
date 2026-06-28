#MAKING FUNCTION STRING_ANALYZER()
def analyze_string(s):
    if s=="":
        print("string is null")
        return
    
    #length
    print("THE LENGTH OF THE STRING IS=",len(s))
    #REVERSE
    print("REVERSE=",s[::-1])
    #counting vowels
    count=0
    for ch in s:
        if ch=='a':
            count+=1
        elif ch=='e':
            count+1
        elif ch=='i':
            count+=1
        elif ch=='o':
            count+=1
        elif ch=='u':
            count+=1
        else:
            continue

        print("NUMBER OF VOWELS:",count)

    print("/nCHARACTER/tPOSITIVE/tNEGATIVE")
    for i in range(len(s)):
        print(f"{s[i]}/t/t{i}/t/t {i-len(s)}")  

text=input("ENTER A STRING:")
analyze_string(text)  