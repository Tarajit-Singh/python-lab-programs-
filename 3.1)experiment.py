"""
3.1Implement a python script for checking whether the citizen is eligible for vote or not
"""
age=int(input("enter age :"))
if age>=18:
    print("Citizen is eligible for voting!")
else:
    print("Citizen not eligible for voting!")
    
#output1
enter age :19
Citizen is eligible for voting!
#output2
enter age :15
Citizen not eligible for voting!
