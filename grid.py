#Lerato Moholo



Month = str(input("Enter the month ('January', ...,'December'):\n"))
day = str(input("Enter the start day ('Monday', ..., 'Sunday'):\n"))

if 
if Month == 'A' :
    for j in range(6):
        start = 1 + j*7     #starting point
        end = start + 7            #ending point
        
        for i in range(start,end):
            if 0<= i <10:
                print(f" {i}",end=' ')     #for single digits
                
            else:
                print(i, end=' ')
                
        print()
        
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")