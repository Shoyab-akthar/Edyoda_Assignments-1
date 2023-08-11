#fibinacci series
End = int(input("Enter the end range: "))
value=0
first = 0
second = 1
next=0
for i in range(0,End+1):    
     if next<=i: 
        next=first+second
        second=first                                 
        first=next          
        print(second ,end=",")