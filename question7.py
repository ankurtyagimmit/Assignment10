'''7. Write a python script to print first N even natural numbers in reverse order'''
N=int(input("Enter any natural number:"))
for i in range(1,N+1):
    print(2*N-2*i+2)
