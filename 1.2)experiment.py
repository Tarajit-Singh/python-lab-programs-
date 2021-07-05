#1.2) Implement a python script to purposefully raise Indentation Error and Correct it
#with indentation error
i=1
while i<=10:
print(i)#indentation error
    i+=1
print('i=',i)
#after correcting indentation error
i=1
while i<=10:
    print(i)
    i+=1
print('i=',i)
#output:
1
2
3
4
5
6
7
8
9
10
i= 11
>>>
