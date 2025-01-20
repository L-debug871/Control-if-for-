#program will print a sequence of 7 numbers, starting from that value. 
#12/08/2024
#Lerato Moholo

str_1 = eval(input("Enter a number between -6 and 93: \n"))
if str_1 >-6 and str_1<93:
    for i in range(7):
        str_2= str_1+i
        if str_2>=0 and str_2<10:        #for single digit numbers
            print(f" {str_2}", end=" ")
        else:
            print(str_2, end=' ')
            
else:
    print("Invalid input! The value of 'n' should be between -6 and 93.")