#asks the user to enter a number, n, where -6<n<2
#Starting from n, the program will print out every 7th number in the range n to n+41.

n_1 = eval(input("Enter a number between -6 and 2:\n"))
if n_1 >-6 and n_1<2:
    for i in range(6):
        n_2 = n_1+7*i
        if n_2>=0 and n_2<10:  
            print(f" {n_2}")
        else:
            print(n_2)
            
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")